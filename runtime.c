#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <stdarg.h>
#include <stdbool.h>

typedef struct Cell {
    char* value;        
    char* type;       
    struct Cell* next; 
} Cell;

typedef struct Row {
    Cell* cells;        
    struct Row* next;  
} Row;

typedef struct Column {
    char* name;         
    char* type;         
    char* reactive_expr;
    struct Column* next;
} Column;

typedef struct Table {
    char* name;        
    Column* columns;   
    Row* rows;          
    int row_count;      
    int col_count;      
    struct Table* next; 
} Table;

static Table* all_tables = NULL;

typedef struct EvalResult {
    char* value;
    char* type;
    int success;
} EvalResult;

typedef struct Variable {
    char* name;
    char* value;
    char* type;
    struct Variable* next;
} Variable;

typedef enum {
    TOK_NUMBER,
    TOK_VARIABLE,
    TOK_OPERATOR,
    TOK_FUNCTION,
    TOK_LEFT_PAREN,
    TOK_RIGHT_PAREN,
    TOK_COMMA,
    TOK_STRING
} TokenType;

typedef struct Token {
    char* value;
    TokenType type;
    struct Token* next;
} Token;

char* strclone(const char* src);
void strtolower(char* str);
int is_integer(const char* str);
int is_float(const char* str);
int is_date(const char* str);
char* get_value_type(const char* value);
char* unquote_string(const char* str);
int compare_values(const char* val1, const char* val2, const char* type);
Table* create_table(const char* name, int col_count, char** col_names, char** col_types, char** reactive_exprs);
Table* find_table(const char* name);
int get_column_index(Table* table, const char* col_name);
char* get_column_type(Table* table, const char* col_name);
Row* create_row(Table* table, char** values);
void table_insert(Table* table, char** values);
void table_insert_silent(Table* table, char** values);
void table_update(Table* table, char** col_names, char** new_values, int col_count, const char* condition);
char* table_get_cell(Table* table, int row_idx, int col_idx);
char* table_evaluate_reactive(Table* table, int row_idx, const char* expr, char** values);
int table_row_count(Table* table);
int table_col_count(Table* table);
void table_print(Table* table);
Table* table_select(Table* table, const char* columns, const char* condition);
Table* table_join(Table* left, Table* right, const char* condition);
Table* table_filter(Table* table, const char* condition);
Table* table_sort(Table* table, const char* column, int descending);
void free_cell(Cell* cell);
void free_row(Row* row);
void free_column(Column* col);
void free_table(Table* table);
void cleanup_all_tables();

Token* tokenize_expression(const char* expr);
void free_tokens(Token* tokens);
char* evaluate_expression(const char* expr, Variable* vars);
char* evaluate_reactive_expression(const char* expr, Variable* vars);
char* get_variable_value_str(const char* name, Variable* vars);
double get_variable_value_double(const char* name, Variable* vars);
int is_operator_char(char c);
int is_function_start(const char* str);
char* evaluate_function(const char* func_name, char** args, int arg_count, Variable* vars);
char* evaluate_multiline_expression(const char* expr, Variable* vars);
char* evaluate_simple_expression(const char* expr, Variable* vars);

char* table_get_value(Table* table, int row_idx, const char* col_name) {
    if (!table || !col_name || row_idx < 0 || row_idx >= table->row_count) {
        return NULL;
    }
    
    int col_idx = get_column_index(table, col_name);
    if (col_idx == -1) {
        return NULL;
    }
    
    Row* row = table->rows;
    for (int i = 0; i < row_idx && row != NULL; i++) {
        row = row->next;
    }
    
    if (row == NULL) return NULL;
    
    Cell* cell = row->cells;
    for (int i = 0; i < col_idx && cell != NULL; i++) {
        cell = cell->next;
    }
    
    return cell ? cell->value : NULL;
}

char* strclone(const char* src) {
    if (!src) return NULL;
    char* dst = malloc(strlen(src) + 1);
    if (dst) strcpy(dst, src);
    return dst;
}

void strtolower(char* str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int is_integer(const char* str) {
    if (!str || !*str) return 0;
    
    int i = 0;
    if (str[0] == '-') i = 1;
    
    for (; str[i]; i++) {
        if (!isdigit(str[i])) return 0;
    }
    return 1;
}

int is_float(const char* str) {
    if (!str || !*str) return 0;
    
    int i = 0;
    int has_dot = 0;
    int has_digit = 0;
    
    if (str[0] == '-') i = 1;
    
    for (; str[i]; i++) {
        if (str[i] == '.') {
            if (has_dot) return 0;
            has_dot = 1;
        } else if (isdigit(str[i])) {
            has_digit = 1;
        } else {
            return 0;
        }
    }
    return has_digit;
}

int is_date(const char* str) {
    if (!str || strlen(str) != 10) return 0;
    
    if (isdigit(str[0]) && isdigit(str[1]) && isdigit(str[2]) && isdigit(str[3]) &&
        str[4] == '-' && isdigit(str[5]) && isdigit(str[6]) &&
        str[7] == '-' && isdigit(str[8]) && isdigit(str[9])) {
        return 1;
    }
    return 0;
}

char* get_value_type(const char* value) {
    if (!value) return "string";
    
    if (is_integer(value)) return "int";
    if (is_float(value)) return "float";
    if (is_date(value)) return "date";
    if (strcmp(value, "true") == 0 || strcmp(value, "false") == 0) return "bool";
    
    if ((value[0] == '"' && value[strlen(value)-1] == '"') ||
        (value[0] == '\'' && value[strlen(value)-1] == '\'')) {
        return "string";
    }
    
    return "string";
}

char* unquote_string(const char* str) {
    if (!str) return NULL;
    
    int len = strlen(str);
    if (len >= 2 && ((str[0] == '"' && str[len-1] == '"') ||
                     (str[0] == '\'' && str[len-1] == '\''))) {
        char* result = malloc(len - 1);
        strncpy(result, str + 1, len - 2);
        result[len-2] = '\0';
        return result;
    }
    return strclone(str);
}

int compare_values(const char* val1, const char* val2, const char* type) {
    if (!val1 || !val2) return 0;
    
    if (strcmp(type, "int") == 0) {
        int i1 = atoi(val1);
        int i2 = atoi(val2);
        return i1 - i2;
    } else if (strcmp(type, "float") == 0) {
        double f1 = atof(val1);
        double f2 = atof(val2);
        if (f1 < f2) return -1;
        if (f1 > f2) return 1;
        return 0;
    } else if (strcmp(type, "date") == 0) {
        return strcmp(val1, val2);
    } else {
        return strcmp(val1, val2);
    }
}

int is_operator_char(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || 
           c == '%' || c == '^' || c == '=' || c == '<' || 
           c == '>' || c == '!' || c == '&' || c == '|';
}

int is_function_start(const char* str) {
    const char* functions[] = {"if", "sum", "avg", "min", "max", "concat", 
                               "upper", "lower", "round", "abs", "sqrt", "len", NULL};
    for (int i = 0; functions[i]; i++) {
        if (strncmp(str, functions[i], strlen(functions[i])) == 0 &&
            (str[strlen(functions[i])] == '(' || isspace(str[strlen(functions[i])]) || str[strlen(functions[i])] == '\0')) {
            return 1;
        }
    }
    return 0;
}

Token* tokenize_expression(const char* expr) {
    if (!expr) return NULL;
    
    Token* head = NULL;
    Token* tail = NULL;
    int i = 0;
    int len = strlen(expr);
    
    while (i < len) {
        while (i < len && isspace(expr[i])) i++;
        if (i >= len) break;
        
        Token* token = malloc(sizeof(Token));
        token->next = NULL;
        
        if (expr[i] == '(') {
            token->value = strclone("(");
            token->type = TOK_LEFT_PAREN;
            i++;
        } else if (expr[i] == ')') {
            token->value = strclone(")");
            token->type = TOK_RIGHT_PAREN;
            i++;
        } else if (expr[i] == ',') {
            token->value = strclone(",");
            token->type = TOK_COMMA;
            i++;
            
        } else if (is_operator_char(expr[i])) {
            int op_len = 1;
            if (i + 1 < len) {
                char two_chars[3] = {expr[i], expr[i+1], '\0'};
                if (strcmp(two_chars, "==") == 0 || strcmp(two_chars, "!=") == 0 ||
                    strcmp(two_chars, "<=") == 0 || strcmp(two_chars, ">=") == 0 ||
                    strcmp(two_chars, "&&") == 0 || strcmp(two_chars, "||") == 0) {
                    op_len = 2;
                }
            }
            
            token->value = malloc(op_len + 1);
            strncpy(token->value, expr + i, op_len);
            token->value[op_len] = '\0';
            token->type = TOK_OPERATOR;
            i += op_len;
            
        } else if (isdigit(expr[i]) || (expr[i] == '.' && i+1 < len && isdigit(expr[i+1]))) {
            int start = i;
            while (i < len && (isdigit(expr[i]) || expr[i] == '.' || 
                              expr[i] == 'e' || expr[i] == 'E' || 
                              expr[i] == '+' || expr[i] == '-')) i++;
            
            token->value = malloc(i - start + 1);
            strncpy(token->value, expr + start, i - start);
            token->value[i - start] = '\0';
            token->type = TOK_NUMBER;
            
        } else if (expr[i] == '"' || expr[i] == '\'') {
            char quote = expr[i];
            int start = i;
            i++;
            while (i < len && expr[i] != quote) i++;
            if (i < len) i++;
            
            token->value = malloc(i - start + 1);
            strncpy(token->value, expr + start, i - start);
            token->value[i - start] = '\0';
            token->type = TOK_STRING;
            
        } else if (isalpha(expr[i]) || expr[i] == '_') {
            int start = i;
            while (i < len && (isalnum(expr[i]) || expr[i] == '_')) i++;
            
            token->value = malloc(i - start + 1);
            strncpy(token->value, expr + start, i - start);
            token->value[i - start] = '\0';
            
            if (is_function_start(token->value)) {
                token->type = TOK_FUNCTION;
            } else {
                token->type = TOK_VARIABLE;
            }
            
        } else {
            free(token);
            i++;
            continue;
        }
        
        if (!head) {
            head = token;
            tail = token;
        } else {
            tail->next = token;
            tail = token;
        }
    }
    
    return head;
}

void free_tokens(Token* tokens) {
    while (tokens) {
        Token* next = tokens->next;
        free(tokens->value);
        free(tokens);
        tokens = next;
    }
}

char* get_variable_value_str(const char* name, Variable* vars) {
    while (vars) {
        if (strcmp(vars->name, name) == 0) {
            return vars->value;
        }
        vars = vars->next;
    }
    return strclone("0");
}

double get_variable_value_double(const char* name, Variable* vars) {
    while (vars) {
        if (strcmp(vars->name, name) == 0) {
            return atof(vars->value);
        }
        vars = vars->next;
    }
    return 0.0;
}

char* evaluate_function(const char* func_name, char** args, int arg_count, Variable* vars) {
    char* result = malloc(256);
    result[0] = '\0';
    
    if (strcmp(func_name, "if") == 0 && arg_count == 3) {
        double cond = atof(args[0]);
        if (cond != 0) {
            strcpy(result, args[1]);
        } else {
            strcpy(result, args[2]);
        }
    } else if (strcmp(func_name, "sum") == 0) {
        double sum = 0;
        for (int i = 0; i < arg_count; i++) {
            sum += atof(args[i]);
        }
        sprintf(result, "%.2f", sum);
    } else if (strcmp(func_name, "avg") == 0) {
        double sum = 0;
        for (int i = 0; i < arg_count; i++) {
            sum += atof(args[i]);
        }
        sprintf(result, "%.2f", arg_count > 0 ? sum / arg_count : 0);
    } else if (strcmp(func_name, "min") == 0 && arg_count > 0) {
        double min_val = atof(args[0]);
        for (int i = 1; i < arg_count; i++) {
            double val = atof(args[i]);
            if (val < min_val) min_val = val;
        }
        sprintf(result, "%.2f", min_val);
    } else if (strcmp(func_name, "max") == 0 && arg_count > 0) {
        double max_val = atof(args[0]);
        for (int i = 1; i < arg_count; i++) {
            double val = atof(args[i]);
            if (val > max_val) max_val = val;
        }
        sprintf(result, "%.2f", max_val);
    } else if (strcmp(func_name, "concat") == 0) {
        result[0] = '\0';
        for (int i = 0; i < arg_count; i++) {
            char* arg = args[i];
            if (arg[0] == '"' && arg[strlen(arg)-1] == '"') {
                char* unquoted = malloc(strlen(arg) - 1);
                strncpy(unquoted, arg + 1, strlen(arg) - 2);
                unquoted[strlen(arg)-2] = '\0';
                strcat(result, unquoted);
                free(unquoted);
            } else {
                strcat(result, arg);
            }
        }
    } else if (strcmp(func_name, "upper") == 0 && arg_count == 1) {
        strcpy(result, args[0]);
        for (int i = 0; result[i]; i++) {
            result[i] = toupper(result[i]);
        }
    } else if (strcmp(func_name, "lower") == 0 && arg_count == 1) {
        strcpy(result, args[0]);
        for (int i = 0; result[i]; i++) {
            result[i] = tolower(result[i]);
        }
    } else if (strcmp(func_name, "round") == 0) {
        double val = atof(args[0]);
        int decimals = arg_count > 1 ? atoi(args[1]) : 0;
        char format[20];
        sprintf(format, "%%.%df", decimals);
        sprintf(result, format, val);
    } else if (strcmp(func_name, "abs") == 0 && arg_count == 1) {
        double val = atof(args[0]);
        sprintf(result, "%.2f", fabs(val));
    } else if (strcmp(func_name, "sqrt") == 0 && arg_count == 1) {
        double val = atof(args[0]);
        if (val >= 0) {
            sprintf(result, "%.2f", sqrt(val));
        } else {
            strcpy(result, "0");
        }
    } else if (strcmp(func_name, "len") == 0 && arg_count == 1) {
        int length = strlen(args[0]);
        if (args[0][0] == '"' && args[0][strlen(args[0])-1] == '"') {
            length -= 2;
        }
        sprintf(result, "%d", length);
    } else if (strcmp(func_name, "left") == 0 && arg_count == 2) {
        char* str = args[0];
        int n = atoi(args[1]);
        if (n <= 0) {
            strcpy(result, "");
        } else if (n >= strlen(str)) {
            strcpy(result, str);
        } else {
            strncpy(result, str, n);
            result[n] = '\0';
        }
    } else if (strcmp(func_name, "substr") == 0 && arg_count == 3) {
        char* str = args[0];
        int start = atoi(args[1]);
        int length = atoi(args[2]);
        if (start < 1) start = 1;
        if (start > strlen(str)) {
            strcpy(result, "");
        } else {
            int start_idx = start - 1;
            int remaining = strlen(str) - start_idx;
            int copy_len = length < remaining ? length : remaining;
            strncpy(result, str + start_idx, copy_len);
            result[copy_len] = '\0';
        }
    } else {
        strcpy(result, "0");
    }
    
    return result;
}

char* evaluate_expression(const char* expr, Variable* vars) {
    if (!expr || strlen(expr) == 0) {
        return strclone("");
    }
    
    Token* tokens = tokenize_expression(expr);
    if (!tokens) {
        return strclone("");
    }
    
    char* stack[100];
    int stack_top = -1;
    
    Token* current = tokens;
    while (current) {
        if (current->type == TOK_NUMBER || current->type == TOK_STRING || current->type == TOK_VARIABLE) {
            char* value;
            
            if (current->type == TOK_NUMBER) {
                value = strclone(current->value);
            } else if (current->type == TOK_STRING) {
                value = strclone(current->value);
            } else {
                value = get_variable_value_str(current->value, vars);
            }
            
            stack[++stack_top] = value;
        } else if (current->type == TOK_OPERATOR) {
            if (stack_top < 1) {
                free_tokens(tokens);
                return strclone("0");
            }
            
            char* right = stack[stack_top--];
            char* left = stack[stack_top--];
            
            double left_num = atof(left);
            double right_num = atof(right);
            double result_num = 0;
            char* result_str = malloc(256);
            
            if (strcmp(current->value, "+") == 0) {
                result_num = left_num + right_num;
                sprintf(result_str, "%.2f", result_num);
            } else if (strcmp(current->value, "-") == 0) {
                result_num = left_num - right_num;
                sprintf(result_str, "%.2f", result_num);
            } else 
                if (strcmp(current->value, "*") == 0) {
                    double left_num = atof(left); 
                    double right_num = atof(right);
                    result_num = left_num * right_num;
                    sprintf(result_str, "%.2f", result_num); 
            } else if (strcmp(current->value, "/") == 0) {
                if (right_num != 0) {
                    result_num = left_num / right_num;
                    sprintf(result_str, "%.2f", result_num);
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, "%") == 0) {
                result_num = fmod(left_num, right_num);
                sprintf(result_str, "%.2f", result_num);
            } else if (strcmp(current->value, "^") == 0) {
                result_num = pow(left_num, right_num);
                sprintf(result_str, "%.2f", result_num);
            } else if (strcmp(current->value, "==") == 0) {
                if (strcmp(left, right) == 0) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, "!=") == 0) {
                if (strcmp(left, right) != 0) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, "<") == 0) {
                if (left_num < right_num) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, "<=") == 0) {
                if (left_num <= right_num) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, ">") == 0) {
                if (left_num > right_num) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, ">=") == 0) {
                if (left_num >= right_num) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, "&&") == 0) {
                if (left_num != 0 && right_num != 0) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else if (strcmp(current->value, "||") == 0) {
                if (left_num != 0 || right_num != 0) {
                    strcpy(result_str, "1");
                } else {
                    strcpy(result_str, "0");
                }
            } else {
                strcpy(result_str, "0");
            }
            
            free(left);
            free(right);
            stack[++stack_top] = result_str;
        }
        
        current = current->next;
    }
    
    free_tokens(tokens);
    
    if (stack_top >= 0) {
        return stack[stack_top];
    } else {
        return strclone("");
    }
}

char* evaluate_reactive_expression(const char* expr, Variable* vars) {
    return evaluate_expression(expr, vars);
}

Table* create_table(const char* name, int col_count, char** col_names, char** col_types, char** reactive_exprs) {
    Table* table = (Table*)malloc(sizeof(Table));
    table->name = strclone(name);
    table->row_count = 0;
    table->col_count = col_count;
    table->rows = NULL;
    table->next = NULL;
    
    Column* last_col = NULL;
    for (int i = 0; i < col_count; i++) {
        Column* col = (Column*)malloc(sizeof(Column));
        col->name = strclone(col_names[i]);
        col->type = strclone(col_types[i]);
        col->reactive_expr = reactive_exprs[i] ? strclone(reactive_exprs[i]) : NULL;
        col->next = NULL;
        
        if (last_col == NULL) {
            table->columns = col;
        } else {
            last_col->next = col;
        }
        last_col = col;
    }
    
    if (all_tables == NULL) {
        all_tables = table;
    } else {
        Table* current = all_tables;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = table;
    }
    
    printf("Table '%s' created with %d columns\n", name, col_count);
    return table;
}

Table* find_table(const char* name) {
    Table* current = all_tables;
    while (current != NULL) {
        if (strcmp(current->name, name) == 0) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

int get_column_index(Table* table, const char* col_name) {
    Column* col = table->columns;
    int index = 0;
    
    while (col != NULL) {
        if (strcmp(col->name, col_name) == 0) {
            return index;
        }
        
        char* dot_pos = strchr(col->name, '.');
        if (dot_pos && strcmp(dot_pos + 1, col_name) == 0) {
            return index;
        }
        
        col = col->next;
        index++;
    }
    
    col = table->columns;
    index = 0;
    while (col != NULL) {
        if (strstr(col->name, col_name) != NULL) {
            char* pos = strstr(col->name, col_name);
            int name_len = strlen(col_name);
            char next_char = *(pos + name_len);
            if (next_char == '\0' || next_char == '.') {
                return index;
            }
        }
        col = col->next;
        index++;
    }
    
    return -1;
}

char* get_column_type(Table* table, const char* col_name) {
    Column* col = table->columns;
    
    while (col != NULL) {
        if (strcmp(col->name, col_name) == 0) {
            return col->type;
        }
        
        char* dot_pos = strchr(col->name, '.');
        if (dot_pos && strcmp(dot_pos + 1, col_name) == 0) {
            return col->type;
        }
        
        col = col->next;
    }
    
    return NULL;
}

Row* create_row(Table* table, char** values) {
    Row* row = (Row*)malloc(sizeof(Row));
    row->cells = NULL;
    row->next = NULL;
    
    Cell* last_cell = NULL;
    Column* col = table->columns;
    int i = 0;
    
    while (col != NULL && i < table->col_count) {
        Cell* cell = (Cell*)malloc(sizeof(Cell));
        cell->type = strclone(col->type);
        
        if (values[i] != NULL && strlen(values[i]) > 0) {
            if (strcmp(col->type, "string") == 0) {
                cell->value = unquote_string(values[i]);
            } else {
                cell->value = strclone(values[i]);
            }
        } else {
            cell->value = strclone("");
        }
        
        cell->next = NULL;
        
        if (last_cell == NULL) {
            row->cells = cell;
        } else {
            last_cell->next = cell;
        }
        last_cell = cell;
        
        col = col->next;
        i++;
    }

    col = table->columns;
    Cell* current_cell = row->cells;
    i = 0;
    
    while (col != NULL && current_cell != NULL) {
        if (col->reactive_expr != NULL && strlen(col->reactive_expr) > 0) {
            
            Variable* vars = NULL;
            Variable* last_var = NULL;
            
            Column* temp_col = table->columns;
            Cell* temp_cell = row->cells;
            int j = 0;
            
            while (temp_col != NULL && temp_cell != NULL) {
                Variable* var = (Variable*)malloc(sizeof(Variable));
                var->name = strclone(temp_col->name);
                
                var->value = temp_cell->value ? temp_cell->value : "";
                var->type = strclone(temp_col->type);
                var->next = NULL;
                
                if (last_var == NULL) {
                    vars = var;
                } else {
                    last_var->next = var;
                }
                last_var = var;
                
                temp_col = temp_col->next;
                temp_cell = temp_cell->next;
                j++;
            }
            
            char* computed_value = evaluate_simple_expression(col->reactive_expr, vars);
            
            Variable* var_to_free = vars;
            while (var_to_free != NULL) {
                Variable* next = var_to_free->next;
                free(var_to_free->name);
                free(var_to_free->type);
                free(var_to_free);
                var_to_free = next;
            }
            
            if (computed_value != NULL && strlen(computed_value) > 0) {
                
                if (current_cell->value != NULL) {
                    free(current_cell->value);
                }
                current_cell->value = computed_value;
            } else {
                if (current_cell->value != NULL) {
                    free(current_cell->value);
                }
                current_cell->value = strclone("");
            }
        }
        
        col = col->next;
        current_cell = current_cell->next;
        i++;
    }
    
    return row;
}

void table_insert(Table* table, char** values) {
    if (!table) return;
    
    Row* new_row = create_row(table, values);
    
    if (table->rows == NULL) {
        table->rows = new_row;
    } else {
        Row* current = table->rows;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = new_row;
    }
    
    table->row_count++;
    printf("Inserted 1 row into table '%s'\n", table->name);
}

void table_insert_silent(Table* table, char** values) {
    if (!table) return;

    Row* new_row = create_row(table, values);

    if (table->rows == NULL) {
        table->rows = new_row;
    } else {
        Row* current = table->rows;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = new_row;
    }

    table->row_count++;
}

void replace_dot_comma(char* s) {
    if (!s) return;
    for (; *s; ++s) {
        if (*s == '.') *s = ',';
    }
}

void table_update(Table* table, char** col_names, char** new_values, int col_count, const char* condition) {
    if (!table || !col_names || !new_values || col_count <= 0) return;
    
    printf("Updating table '%s' with %d columns, condition: %s\n", 
           table->name, col_count, condition ? condition : "none");
    
    int* col_indices = (int*)malloc(col_count * sizeof(int));
    for (int i = 0; i < col_count; i++) {
        col_indices[i] = get_column_index(table, col_names[i]);
        if (col_indices[i] == -1) {
            printf("Warning: Column '%s' not found\n", col_names[i]);
            free(col_indices);
            return;
        }
    }
    
    Row* row = table->rows;
    int updated_count = 0;
    
    while (row != NULL) {
        int should_update = 1;
        
        if (condition && strlen(condition) > 0 && strcmp(condition, "1") != 0) {
            char cond_copy[256];
            strcpy(cond_copy, condition);
            
            char* column = NULL;
            char* op = NULL;
            char* value = NULL;
            
            char* eq_pos = strstr(cond_copy, "==");
            if (eq_pos) {
                *eq_pos = '\0';
                column = cond_copy;
                value = eq_pos + 2;
                
                while (*column == ' ') column++;
                char* col_end = column + strlen(column) - 1;
                while (col_end > column && *col_end == ' ') *col_end-- = '\0';
                
                while (*value == ' ') value++;
                char* val_end = value + strlen(value) - 1;
                while (val_end > value && *val_end == ' ') *val_end-- = '\0';
                
                int cond_col_idx = get_column_index(table, column);
                if (cond_col_idx != -1) {
                    Cell* cell = row->cells;
                    for (int i = 0; i < cond_col_idx && cell != NULL; i++) {
                        cell = cell->next;
                    }
                    
                    if (cell && cell->value) {
                        char* cell_type = get_column_type(table, column);
                        int cmp = compare_values(cell->value, value, cell_type);
                        should_update = (cmp == 0);
                    } else {
                        should_update = 0;
                    }
                } else {
                    should_update = 0;
                }
            } else {
                should_update = 0;
            }
        }
        
        if (should_update) {
            for (int i = 0; i < col_count; i++) {
                Cell* cell = row->cells;
                for (int j = 0; j < col_indices[i] && cell != NULL; j++) {
                    cell = cell->next;
                }
                
                if (cell) {
                    free(cell->value);
                    cell->value = strclone(new_values[i]);
                }
            }
            
            updated_count++;
            
            Column* col = table->columns;
            Cell* current_cell = row->cells;
            int cell_idx = 0;
            
            while (col != NULL && current_cell != NULL) {
                if (col->reactive_expr && strlen(col->reactive_expr) > 0) {
                    Variable* vars = NULL;
                    Variable* last_var = NULL;
                    
                    Column* temp_col = table->columns;
                    Cell* temp_cell = row->cells;
                    
                    while (temp_col != NULL && temp_cell != NULL) {
                        Variable* var = (Variable*)malloc(sizeof(Variable));
                        var->name = strclone(temp_col->name);
                        var->value = strclone(temp_cell->value ? temp_cell->value : "");
                        var->type = strclone(temp_col->type);
                        var->next = NULL;
                        
                        if (last_var == NULL) {
                            vars = var;
                        } else {
                            last_var->next = var;
                        }
                        last_var = var;
                        
                        temp_col = temp_col->next;
                        temp_cell = temp_cell->next;
                    }
                    
                    char* computed_value = evaluate_reactive_expression(col->reactive_expr, vars);
                    
                    Variable* var_to_free = vars;
                    while (var_to_free != NULL) {
                        Variable* next = var_to_free->next;
                        free(var_to_free->name);
                        free(var_to_free->value);
                        free(var_to_free->type);
                        free(var_to_free);
                        var_to_free = next;
                    }
                    
                    if (computed_value && strlen(computed_value) > 0) {
                        free(current_cell->value);
                        current_cell->value = computed_value;
                    } else {
                        free(computed_value);
                    }
                }
                
                col = col->next;
                current_cell = current_cell->next;
                cell_idx++;
            }
        }
        
        row = row->next;
    }
    
    free(col_indices);
    printf("Updated %d rows in table '%s'\n", updated_count, table->name);
}

char* table_get_cell(Table* table, int row_idx, int col_idx) {
    if (!table || row_idx < 0 || col_idx < 0) return NULL;
    
    Row* row = table->rows;
    for (int i = 0; i < row_idx && row != NULL; i++) {
        row = row->next;
    }
    
    if (row == NULL) return NULL;
    
    Cell* cell = row->cells;
    for (int i = 0; i < col_idx && cell != NULL; i++) {
        cell = cell->next;
    }
    
    return cell ? cell->value : NULL;
}

char* table_evaluate_reactive(Table* table, int row_idx, const char* expr, char** values) {
    if (!table || !expr) return strclone("");

    Variable* vars = NULL;
    Variable* last_var = NULL;
    
    Column* col = table->columns;
    int i = 0;
    
    while (col != NULL && values && values[i]) {
        Variable* var = (Variable*)malloc(sizeof(Variable));
        var->name = strclone(col->name);
        var->value = strclone(values[i]);
        var->type = strclone(col->type);
        var->next = NULL;
        
        if (last_var == NULL) {
            vars = var;
        } else {
            last_var->next = var;
        }
        last_var = var;
        
        col = col->next;
        i++;
    }
    
    char* result = evaluate_reactive_expression(expr, vars);
    
    Variable* var_to_free = vars;
    while (var_to_free != NULL) {
        Variable* next = var_to_free->next;
        free(var_to_free->name);
        free(var_to_free->value);
        free(var_to_free->type);
        free(var_to_free);
        var_to_free = next;
    }
    
    return result;
}

int table_row_count(Table* table) {
    return table ? table->row_count : 0;
}

int table_col_count(Table* table) {
    return table ? table->col_count : 0;
}

void print_separator(int* col_widths, int col_count) {
    printf("+");
    for (int i = 0; i < col_count; i++) {
        for (int j = 0; j < col_widths[i] + 2; j++) {
            printf("-");
        }
        printf("+");
    }
    printf("\n");
}

void table_print(Table* table) {
    if (!table) {
        printf("Table is NULL\n");
        return;
    }
    
    printf("\nTable: %s (%d rows, %d columns)\n", table->name, table->row_count, table->col_count);
    
    Column* col = table->columns;
    while (col != NULL) {
        if (col->reactive_expr && strlen(col->reactive_expr) > 0) {
            printf("  Column '%s' is reactive: %s\n", col->name, col->reactive_expr);
        }
        col = col->next;
    }
    
    if (table->row_count == 0) {
        printf("(empty table)\n");
        return;
    }
    
    int col_widths[table->col_count];
    for (int i = 0; i < table->col_count; i++) col_widths[i] = 0;
    
    col = table->columns;
    int col_idx = 0;
    while (col != NULL) {
        int len = strlen(col->name);
        if (len > col_widths[col_idx]) {
            col_widths[col_idx] = len;
        }
        col = col->next;
        col_idx++;
    }
    
    Row* row = table->rows;
    while (row != NULL) {
        Cell* cell = row->cells;
        col_idx = 0;
        while (cell != NULL) {
            if (cell->value) {
                int len = strlen(cell->value);
                if (len > col_widths[col_idx]) {
                    col_widths[col_idx] = len;
                }
            }
            cell = cell->next;
            col_idx++;
        }
        row = row->next;
    }
    
    print_separator(col_widths, table->col_count);
    
    printf("|");
    col = table->columns;
    col_idx = 0;
    while (col != NULL) {
        printf(" %-*s |", col_widths[col_idx], col->name);
        col = col->next;
        col_idx++;
    }
    printf("\n");
    
    print_separator(col_widths, table->col_count);
    
    row = table->rows;
    while (row != NULL) {
        printf("|");
        Cell* cell = row->cells;
        col_idx = 0;
        while (cell != NULL) {
            printf(" %-*s |", col_widths[col_idx], cell->value ? cell->value : "");
            cell = cell->next;
            col_idx++;
        }
        printf("\n");
        row = row->next;
    }
    
    print_separator(col_widths, table->col_count);
    printf("\n");
}

int check_single_condition(Table* table, Row* row, const char* condition) {
    if (!condition || strlen(condition) == 0 || strcmp(condition, "1") == 0) {
        return 1;
    }
    
    char cond_copy[256];
    strncpy(cond_copy, condition, sizeof(cond_copy)-1);
    cond_copy[sizeof(cond_copy)-1] = '\0';
    
    char* cond = cond_copy;
    while (*cond == ' ') cond++;
    int len = strlen(cond);
    while (len > 0 && cond[len-1] == ' ') {
        cond[len-1] = '\0';
        len--;
    }
    
    if (strstr(cond, "LEFT(") != NULL) {
        char* left_start = strstr(cond, "LEFT(");
        char* comma = strchr(left_start, ',');
        char* close_paren = strchr(left_start, ')');
        
        if (comma && close_paren && comma < close_paren) {
            *comma = '\0';
            char* column_name = left_start + 5;
            *close_paren = '\0';
            char* num_str = comma + 1;
            
            while (*column_name == ' ') column_name++;
            while (*num_str == ' ') num_str++;
            
            int col_idx = get_column_index(table, column_name);
            if (col_idx == -1) return 0;
            
            Cell* cell = row->cells;
            for (int i = 0; i < col_idx && cell != NULL; i++) {
                cell = cell->next;
            }
            
            if (!cell || !cell->value) return 0;
            
            int n = atoi(num_str);
            char left_value[256];
            if (n <= 0) {
                left_value[0] = '\0';
            } else if (n >= strlen(cell->value)) {
                strcpy(left_value, cell->value);
            } else {
                strncpy(left_value, cell->value, n);
                left_value[n] = '\0';
            }
            
            char* equal_op = strstr(close_paren + 1, "=");
            if (!equal_op) return 0;
            
            char* value_str = equal_op + 1;
            while (*value_str == ' ') value_str++;
            
            if ((*value_str == '\'' || *value_str == '"') && 
                value_str[strlen(value_str)-1] == *value_str) {
                value_str++;
                value_str[strlen(value_str)-1] = '\0';
            }
            
            return strcmp(left_value, value_str) == 0;
        }
        return 0;
    }
    
    char* op_pos = NULL;
    char* operators[] = {">=", "<=", "==", "!=", ">", "<"};
    char* op = NULL;
    
    for (int i = 0; i < 6; i++) {
        op_pos = strstr(cond, operators[i]);
        if (op_pos != NULL) {
            op = operators[i];
            break;
        }
    }
    
    if (op == NULL) {
        return 1;
    }
    
    *op_pos = '\0';
    char* column_name = cond;
    char* value_str = op_pos + strlen(op);
    
    while (*column_name == ' ') column_name++;
    while (*value_str == ' ') value_str++;
    
    if ((*value_str == '\'' || *value_str == '"') && 
        value_str[strlen(value_str)-1] == *value_str) {
        value_str++;
        value_str[strlen(value_str)-1] = '\0';
    }
    
    int col_idx = get_column_index(table, column_name);
    if (col_idx == -1) return 0;
    
    Cell* cell = row->cells;
    for (int i = 0; i < col_idx && cell != NULL; i++) {
        cell = cell->next;
    }
    
    if (!cell || !cell->value) return 0;
    
    char* col_type = get_column_type(table, column_name);
    int cmp = compare_values(cell->value, value_str, col_type);
    
    if (strcmp(op, "==") == 0) return cmp == 0;
    if (strcmp(op, "!=") == 0) return cmp != 0;
    if (strcmp(op, ">") == 0) return cmp > 0;
    if (strcmp(op, "<") == 0) return cmp < 0;
    if (strcmp(op, ">=") == 0) return cmp >= 0;
    if (strcmp(op, "<=") == 0) return cmp <= 0;
    
    return 0;
}

int check_row_condition(Table* table, Row* row, const char* condition) {
    if (!condition || strlen(condition) == 0 || strcmp(condition, "1") == 0) {
        return 1;
    }
    
    char cond_copy[256];
    strncpy(cond_copy, condition, sizeof(cond_copy)-1);
    cond_copy[sizeof(cond_copy)-1] = '\0';
    
    int and_count = 0;
    char* and_parts[10];
    char* token = strtok(cond_copy, " ");
    char current_part[256] = "";
    
    while (token != NULL) {
        if (strcmp(token, "and") == 0) {
            and_parts[and_count] = strclone(current_part);
            and_count++;
            current_part[0] = '\0';
        } else {
            if (strlen(current_part) > 0) {
                strcat(current_part, " ");
            }
            strcat(current_part, token);
        }
        token = strtok(NULL, " ");
    }
    
    if (strlen(current_part) > 0) {
        and_parts[and_count] = strclone(current_part);
        and_count++;
    }
    
    int result = 1;
    for (int i = 0; i < and_count; i++) {
        if (!check_single_condition(table, row, and_parts[i])) {
            result = 0;
        }
        free(and_parts[i]);
    }
    
    return result;
}

Table* table_select(Table* table, const char* columns, const char* condition) {
    if (!table) return NULL;
    
    char result_name[256];
    snprintf(result_name, sizeof(result_name), "%s_select", table->name);
    
    int include_all = (strcmp(columns, "*") == 0);
    char* cols_copy = strclone(columns);
    char* col_names[table->col_count];
    char* col_types[table->col_count];
    char* reactive_exprs[table->col_count];
    int col_count = 0;
    
    if (include_all) {
        Column* col = table->columns;
        while (col != NULL) {
            col_names[col_count] = strclone(col->name);
            col_types[col_count] = strclone(col->type);
            reactive_exprs[col_count] = col->reactive_expr ? strclone(col->reactive_expr) : NULL;
            col_count++;
            col = col->next;
        }
    } else {
        char* token = strtok(cols_copy, ",");
        while (token != NULL) {
            while (*token == ' ') token++;
            char* end = token + strlen(token) - 1;
            while (end > token && *end == ' ') *end-- = '\0';
            
            if (get_column_index(table, token) != -1) {
                Column* col = table->columns;
                while (col != NULL) {
                    if (strcmp(col->name, token) == 0) {
                        col_names[col_count] = strclone(col->name);
                        col_types[col_count] = strclone(col->type);
                        reactive_exprs[col_count] = col->reactive_expr ? strclone(col->reactive_expr) : NULL;
                        col_count++;
                        break;
                    }
                    col = col->next;
                }
            }
            token = strtok(NULL, ",");
        }
    }
    
    free(cols_copy);
    
    Table* result = create_table(result_name, col_count, col_names, col_types, reactive_exprs);
    
    for (int i = 0; i < col_count; i++) {
        free(col_names[i]);
        free(col_types[i]);
        if (reactive_exprs[i]) free(reactive_exprs[i]);
    }
    
    Row* src_row = table->rows;
    while (src_row != NULL) {
        if (check_row_condition(table, src_row, condition)) {
            char** values = (char**)calloc(col_count, sizeof(char*));
            
            for (int i = 0; i < col_count; i++) {
                int src_col_idx = -1;
                if (include_all) {
                    src_col_idx = i;
                } else {
                    char* col_name = NULL;
                    Column* col = result->columns;
                    for (int j = 0; j < i && col != NULL; j++) {
                        col = col->next;
                    }
                    if (col) {
                        src_col_idx = get_column_index(table, col->name);
                    }
                }
                
                if (src_col_idx != -1) {
                    Cell* cell = src_row->cells;
                    for (int j = 0; j < src_col_idx && cell != NULL; j++) {
                        cell = cell->next;
                    }
                    if (cell && cell->value) {
                        values[i] = strclone(cell->value);
                    }
                }
            }
            
            table_insert(result, values);
            
            for (int i = 0; i < col_count; i++) {
                if (values[i]) free(values[i]);
            }
            free(values);
        }
        
        src_row = src_row->next;
    }
    
    return result;
}

Table* table_join(Table* left, Table* right, const char* condition) {
    if (!left || !right || !condition) return NULL;
    
    char result_name[256];
    snprintf(result_name, sizeof(result_name), "%s_join_%s", left->name, right->name);
    
   char cond_copy[256];
    strncpy(cond_copy, condition, sizeof(cond_copy)-1);
    cond_copy[sizeof(cond_copy)-1] = '\0';

    printf("Join condition: '%s'\n", cond_copy);
    printf("Left table: '%s', Right table: '%s'\n", left->name, right->name);
    
    char* dot1 = strchr(cond_copy, '.');
    char* equal = strstr(cond_copy, "=");
    char* dot2 = equal ? strchr(equal + 1, '.') : NULL;
    
    if (!dot1 || !equal || !dot2) {
        printf("Invalid join condition format. Expected: left.column = right.column\n");
        return NULL;
    }
    
    *dot1 = '\0';
    *equal = '\0';
    *dot2 = '\0';
    
    char* left_table_name = cond_copy;
    char* left_column_name = dot1 + 1;
    char* right_table_name = equal + 1;
    char* right_column_name = dot2 + 1;
    
    if (strcmp(left_table_name, left->name) != 0 || 
        strcmp(right_table_name, right->name) != 0) {
        printf("Table names in condition don't match\n");
        return NULL;
    }
    
    int left_col_idx = get_column_index(left, left_column_name);
    int right_col_idx = get_column_index(right, right_column_name);
    
    if (left_col_idx == -1 || right_col_idx == -1) {
        printf("Join columns not found\n");
        return NULL;
    }
    
    int total_cols = left->col_count + right->col_count;
    char** col_names = (char**)malloc(total_cols * sizeof(char*));
    char** col_types = (char**)malloc(total_cols * sizeof(char*));
    char** reactive_exprs = (char**)calloc(total_cols, sizeof(char*));
    
    Column* col = left->columns;
    int idx = 0;
    while (col != NULL) {
        char name[256];
        snprintf(name, sizeof(name), "%s.%s", left->name, col->name);
        col_names[idx] = strclone(name);
        col_types[idx] = strclone(col->type);
        reactive_exprs[idx] = col->reactive_expr ? strclone(col->reactive_expr) : NULL;
        idx++;
        col = col->next;
    }
    
    col = right->columns;
    while (col != NULL) {
        char name[256];
        snprintf(name, sizeof(name), "%s.%s", right->name, col->name);
        col_names[idx] = strclone(name);
        col_types[idx] = strclone(col->type);
        reactive_exprs[idx] = col->reactive_expr ? strclone(col->reactive_expr) : NULL;
        idx++;
        col = col->next;
    }
    
    Table* result = create_table(result_name, total_cols, col_names, col_types, reactive_exprs);
    
    for (int i = 0; i < total_cols; i++) {
        free(col_names[i]);
        free(col_types[i]);
        if (reactive_exprs[i]) free(reactive_exprs[i]);
    }
    free(col_names);
    free(col_types);
    free(reactive_exprs);
    
    Row* left_row = left->rows;
    while (left_row != NULL) {
        Cell* left_cell = left_row->cells;
        for (int i = 0; i < left_col_idx && left_cell != NULL; i++) {
            left_cell = left_cell->next;
        }
        
        if (!left_cell || !left_cell->value) {
            left_row = left_row->next;
            continue;
        }
        
        Row* right_row = right->rows;
        while (right_row != NULL) {
            Cell* right_cell = right_row->cells;
            for (int i = 0; i < right_col_idx && right_cell != NULL; i++) {
                right_cell = right_cell->next;
            }
            
            if (right_cell && right_cell->value && 
                strcmp(left_cell->value, right_cell->value) == 0) {
                char** values = (char**)calloc(total_cols, sizeof(char*));
                
                Cell* cell = left_row->cells;
                int val_idx = 0;
                while (cell != NULL) {
                    values[val_idx++] = strclone(cell->value);
                    cell = cell->next;
                }
                
                cell = right_row->cells;
                while (cell != NULL) {
                    values[val_idx++] = strclone(cell->value);
                    cell = cell->next;
                }
                
                table_insert(result, values);

                for (int i = 0; i < total_cols; i++) {
                    if (values[i]) free(values[i]);
                }
                free(values);
            }
            
            right_row = right_row->next;
        }
        
        left_row = left_row->next;
    }
    
    return result;
}

Table* table_filter(Table* table, const char* condition) {
    if (!table) return NULL;
    
    char result_name[256];
    snprintf(result_name, sizeof(result_name), "%s_filtered", table->name);
    
    Column* col = table->columns;
    int col_count = 0;
    char** col_names = NULL;
    char** col_types = NULL;
    char** reactive_exprs = NULL;
    
    while (col != NULL) {
        col_count++;
        col = col->next;
    }
    
    col_names = (char**)malloc(col_count * sizeof(char*));
    col_types = (char**)malloc(col_count * sizeof(char*));
    reactive_exprs = (char**)calloc(col_count, sizeof(char*));
    
    col = table->columns;
    for (int i = 0; i < col_count; i++) {
        col_names[i] = strclone(col->name);
        col_types[i] = strclone(col->type);
        reactive_exprs[i] = col->reactive_expr ? strclone(col->reactive_expr) : NULL;
        col = col->next;
    }
    
    Table* result = create_table(result_name, col_count, col_names, col_types, reactive_exprs);
    
    for (int i = 0; i < col_count; i++) {
        free(col_names[i]);
        free(col_types[i]);
        if (reactive_exprs[i]) free(reactive_exprs[i]);
    }
    free(col_names);
    free(col_types);
    free(reactive_exprs);
    
    Row* row = table->rows;
    while (row != NULL) {
        if (check_row_condition(table, row, condition)) {
            char** values = (char**)malloc(col_count * sizeof(char*));
            Cell* cell = row->cells;
            for (int i = 0; i < col_count; i++) {
                values[i] = cell ? strclone(cell->value) : strclone("");
                if (cell) cell = cell->next;
            }
            
            table_insert(result, values);
            
            for (int i = 0; i < col_count; i++) {
                free(values[i]);
            }
            free(values);
        }
        row = row->next;
    }
    
    return result;
}

char* evaluate_arithmetic_expression(const char* expr, Variable* vars) {
    if (!expr) return strclone("");
    
    
    char expr_copy[256];
    strncpy(expr_copy, expr, sizeof(expr_copy) - 1);
    expr_copy[sizeof(expr_copy) - 1] = '\0';
    
    char* operators[] = {"*", "/", "+", "-"};
    char* op = NULL;
    char* op_pos = NULL;
    
    for (int i = 0; i < 4; i++) {
        op_pos = strstr(expr_copy, operators[i]);
        if (op_pos != NULL) {
            op = operators[i];
            break;
        }
    }
    
    if (!op) {
        if (is_float(expr_copy) || is_integer(expr_copy)) {
            return strclone(expr_copy);
        }
        
        Variable* current = vars;
        while (current != NULL) {
            if (strcmp(current->name, expr_copy) == 0) {
                return strclone(current->value);
            }
            current = current->next;
        }
        
        return strclone("0");
    }
    
    *op_pos = '\0';
    char* left_expr = expr_copy;
    char* right_expr = op_pos + strlen(op);
    
    while (*left_expr == ' ') left_expr++;
    char* left_end = left_expr + strlen(left_expr) - 1;
    while (left_end > left_expr && *left_end == ' ') {
        *left_end = '\0';
        left_end--;
    }
    
    while (*right_expr == ' ') right_expr++;
    char* right_end = right_expr + strlen(right_expr) - 1;
    while (right_end > right_expr && *right_end == ' ') {
        *right_end = '\0';
        right_end--;
    }
    
    
    double left_val = 0.0;
    if (is_float(left_expr) || is_integer(left_expr)) {
        left_val = atof(left_expr);
    } else {
        Variable* current = vars;
        while (current != NULL) {
            if (strcmp(current->name, left_expr) == 0) {
                left_val = atof(current->value);
                break;
            }
            current = current->next;
        }
    }
    
    double right_val = 0.0;
    if (is_float(right_expr) || is_integer(right_expr)) {
        right_val = atof(right_expr);
    } else {
        Variable* current = vars;
        while (current != NULL) {
            if (strcmp(current->name, right_expr) == 0) {
                right_val = atof(current->value);
                break;
            }
            current = current->next;
        }
    }
    
    double result = 0.0;
    if (strcmp(op, "*") == 0) {
        result = left_val * right_val;
    } else if (strcmp(op, "/") == 0) {
        if (right_val != 0.0) {
            result = left_val / right_val;
        }
    } else if (strcmp(op, "+") == 0) {
        result = left_val + right_val;
    } else if (strcmp(op, "-") == 0) {
        result = left_val - right_val;
    }
    
    char* result_str = malloc(32);
    sprintf(result_str, "%.2f", result);
    
    return result_str;
}

char* evaluate_simple_expression(const char* expr, Variable* vars) {
    if (!expr || strlen(expr) == 0) {
        return strclone("");
    }
    
    return evaluate_arithmetic_expression(expr, vars);
}

char* evaluate_multiline_expression(const char* expr, Variable* vars) {
    if (!expr) return strclone("");
    
    char* simplified = strclone(expr);
    
    char* pos;
    
    while ((pos = strstr(simplified, "if")) != NULL) {
        char* colon = strstr(pos, ":");
        if (colon) {
            char* else_pos = strstr(colon, "else:");
            if (else_pos) {
                *colon = '\0';
                char* condition = pos + 2;
                char* true_val = colon + 1;
                *else_pos = '\0';
                char* false_val = else_pos + 5;
                
                char new_expr[1024];
                snprintf(new_expr, sizeof(new_expr), "if(%s, %s, %s)", 
                        condition, true_val, false_val);
                
                char* result = malloc(strlen(simplified) + strlen(new_expr) + 1);
                sprintf(result, "%.*s%s%s", 
                        (int)(pos - simplified), simplified,
                        new_expr,
                        false_val + strlen(false_val));
                
                free(simplified);
                simplified = result;
            }
        }
        break;
    }
    
    pos = strstr(simplified, "return");
    if (pos) {
        memmove(pos, pos + 6, strlen(pos + 6) + 1);
    }
    
    char* result = evaluate_expression(simplified, vars);
    free(simplified);
    
    return result;
}

Table* table_sort(Table* table, const char* column, int descending) {
    if (!table) return NULL;
    
    int sort_col_idx = get_column_index(table, column);
    if (sort_col_idx == -1) {
        char search_name[256];
        if (strchr(column, '.') == NULL) {
            Column* col = table->columns;
            while (col != NULL) {
                char* dot_pos = strchr(col->name, '.');
                if (dot_pos && strcmp(dot_pos + 1, column) == 0) {
                    strcpy(search_name, col->name);
                    sort_col_idx = get_column_index(table, col->name);
                    break;
                }
                col = col->next;
            }
        }
        
        if (sort_col_idx == -1) {
            printf("Column '%s' not found for sorting\n", column);
            return NULL;
        }
    }
    
    char result_name[256];
    snprintf(result_name, sizeof(result_name), "%s_sorted", table->name);
    
    Column* col = table->columns;
    int col_count = 0;
    while (col != NULL) {
        col_count++;
        col = col->next;
    }
    
    char** col_names = (char**)malloc(col_count * sizeof(char*));
    char** col_types = (char**)malloc(col_count * sizeof(char*));
    char** reactive_exprs = (char**)calloc(col_count, sizeof(char*));
    
    col = table->columns;
    for (int i = 0; i < col_count; i++) {
        col_names[i] = strclone(col->name);
        col_types[i] = strclone(col->type);
        reactive_exprs[i] = col->reactive_expr ? strclone(col->reactive_expr) : NULL;
        col = col->next;
    }
    
    Table* result = create_table(result_name, col_count, col_names, col_types, reactive_exprs);
    
    for (int i = 0; i < col_count; i++) {
        free(col_names[i]);
        free(col_types[i]);
        if (reactive_exprs[i]) free(reactive_exprs[i]);
    }
    free(col_names);
    free(col_types);
    free(reactive_exprs);
    
    if (table->row_count == 0) {
        return result;
    }
    
    Row** rows = (Row**)malloc(table->row_count * sizeof(Row*));
    Row* row = table->rows;
    int row_count = 0;
    
    while (row != NULL) {
        rows[row_count++] = row;
        row = row->next;
    }
    
    char* actual_col_name = NULL;
    col = table->columns;
    for (int i = 0; i < sort_col_idx && col != NULL; i++) {
        col = col->next;
    }
    if (col) {
        actual_col_name = col->name;
    }
    
    char* sort_col_type = get_column_type(table, actual_col_name ? actual_col_name : column);
    
    for (int i = 0; i < row_count - 1; i++) {
        for (int j = 0; j < row_count - i - 1; j++) {
            Cell* cell1 = rows[j]->cells;
            Cell* cell2 = rows[j+1]->cells;
            
            for (int k = 0; k < sort_col_idx && cell1 != NULL && cell2 != NULL; k++) {
                cell1 = cell1->next;
                cell2 = cell2->next;
            }
            
            char* val1 = cell1 ? cell1->value : NULL;
            char* val2 = cell2 ? cell2->value : NULL;
            
            int cmp = compare_values(val1, val2, sort_col_type);
            
            if ((!descending && cmp > 0) || (descending && cmp < 0)) {
                Row* temp = rows[j];
                rows[j] = rows[j+1];
                rows[j+1] = temp;
            }
        }
    }
    
    for (int i = 0; i < row_count; i++) {
        char** values = (char**)malloc(col_count * sizeof(char*));
        Cell* cell = rows[i]->cells;
        
        for (int j = 0; j < col_count; j++) {
            values[j] = cell ? strclone(cell->value) : strclone("");
            if (cell) cell = cell->next;
        }
        
        table_insert(result, values);
        
        for (int j = 0; j < col_count; j++) {
            free(values[j]);
        }
        free(values);
    }
    
    free(rows);
    return result;
}

void free_cell(Cell* cell) {
    if (!cell) return;
    if (cell->value) free(cell->value);
    if (cell->type) free(cell->type);
    free(cell);
}

void free_row(Row* row) {
    while (row != NULL) {
        Row* next_row = row->next;
        
        Cell* cell = row->cells;
        while (cell != NULL) {
            Cell* next_cell = cell->next;
            free_cell(cell);
            cell = next_cell;
        }
        
        free(row);
        row = next_row;
    }
}

void free_column(Column* col) {
    while (col != NULL) {
        Column* next_col = col->next;
        if (col->name) free(col->name);
        if (col->type) free(col->type);
        if (col->reactive_expr) free(col->reactive_expr);
        free(col);
        col = next_col;
    }
}

void free_table(Table* table) {
    if (!table) return;
    
    if (table->name) free(table->name);
    free_column(table->columns);
    free_row(table->rows);
    free(table);
}

void cleanup_all_tables() {
    Table* current = all_tables;
    while (current != NULL) {
        Table* next = current->next;
        free_table(current);
        current = next;
    }
    all_tables = NULL;
}