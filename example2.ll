; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i8* @"create_table"(i8* %".1", i32 %".2", i8** %".3", i8** %".4", i8** %".5")

declare i8* @"find_table"(i8* %".1")

declare void @"table_insert"(i8* %".1", i8** %".2")

declare void @"table_insert_silent"(i8* %".1", i8** %".2")

declare void @"table_update"(i8* %".1", i8** %".2", i8** %".3", i32 %".4", i8* %".5")

declare void @"table_print"(i8* %".1")

declare i8* @"table_select"(i8* %".1", i8* %".2", i8* %".3")

declare i8* @"table_join"(i8* %".1", i8* %".2", i8* %".3")

declare i8* @"table_filter"(i8* %".1", i8* %".2")

declare i8* @"table_sort"(i8* %".1", i8* %".2", i32 %".3")

declare i8* @"evaluate_expression"(i8* %".1", i8* %".2")

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

declare i8* @"malloc"(i64 %".1")

declare void @"free"(i8* %".1")

declare i32 @"atoi"(i8* %".1")

declare double @"atof"(i8* %".1")

declare i8* @"strdup"(i8* %".1")

declare i32 @"strcmp"(i8* %".1", i8* %".2")

declare i8* @"strcat"(i8* %".1", i8* %".2")

declare i64 @"strlen"(i8* %".1")

declare i8* @"strstr"(i8* %".1", i8* %".2")

declare double @"fmod"(double %".1", double %".2")

declare void @"cleanup_all_tables"()

define i32 @"main"()
{
entry:
  %".2" = alloca [1 x i8*]
  %".3" = getelementptr [2 x i8], [2 x i8]* @".str.0", i32 0, i32 0
  %".4" = getelementptr [1 x i8*], [1 x i8*]* %".2", i32 0, i32 0
  store i8* %".3", i8** %".4"
  %".6" = getelementptr [1 x i8*], [1 x i8*]* %".2", i32 0, i32 0
  %".7" = alloca [1 x i8*]
  %".8" = getelementptr [4 x i8], [4 x i8]* @".str.1", i32 0, i32 0
  %".9" = getelementptr [1 x i8*], [1 x i8*]* %".7", i32 0, i32 0
  store i8* %".8", i8** %".9"
  %".11" = getelementptr [1 x i8*], [1 x i8*]* %".7", i32 0, i32 0
  %".12" = alloca [1 x i8*]
  %".13" = getelementptr [1 x i8*], [1 x i8*]* %".12", i32 0, i32 0
  store i8* null, i8** %".13"
  %".15" = getelementptr [1 x i8*], [1 x i8*]* %".12", i32 0, i32 0
  %".16" = getelementptr [8 x i8], [8 x i8]* @".str.2", i32 0, i32 0
  %".17" = call i8* @"create_table"(i8* %".16", i32 1, i8** %".6", i8** %".11", i8** %".15")
  %"i" = alloca i8*
  %"i_counter" = alloca i32
  store i32 1, i32* %"i_counter"
  br label %"for_cond_i"
for_cond_i:
  %".20" = load i32, i32* %"i_counter"
  %".21" = icmp sle i32 %".20", 5
  br i1 %".21", label %"for_body_i", label %"for_end_i"
for_body_i:
  %".23" = alloca [32 x i8]
  %".24" = getelementptr [32 x i8], [32 x i8]* %".23", i32 0, i32 0
  %".25" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".26" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".24", i8* %".25", i32 %".20")
  %".27" = call i8* @"strdup"(i8* %".24")
  store i8* %".27", i8** %"i"
  %".29" = load i8*, i8** %"i"
  %".30" = alloca [1 x i8*]
  %".31" = getelementptr [1 x i8*], [1 x i8*]* %".30", i32 0, i32 0
  store i8* %".29", i8** %".31"
  %".33" = getelementptr [1 x i8*], [1 x i8*]* %".30", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".17", i8** %".33")
  %".35" = add i32 %".20", 1
  store i32 %".35", i32* %"i_counter"
  br label %"for_cond_i"
for_end_i:
  call void @"table_print"(i8* %".17")
  %".39" = load i8*, i8** %"i"
  %".40" = getelementptr [5 x i8], [5 x i8]* @".str.4", i32 0, i32 0
  %"x" = alloca i8*
  store i8* %".40", i8** %"x"
  %".42" = load i8*, i8** %"x"
  %".43" = getelementptr [5 x i8], [5 x i8]* @".str.4", i32 0, i32 0
  %".44" = getelementptr [6 x i8], [6 x i8]* @".str.5", i32 0, i32 0
  %".45" = call i32 @"strcmp"(i8* %".42", i8* %".43")
  %".46" = icmp eq i32 %".45", 0
  br i1 %".46", label %"switch_case", label %"switch_default"
switch_end:
  %".56" = getelementptr [2 x i8], [2 x i8]* @".str.0", i32 0, i32 0
  %".57" = call i8* @"table_select"(i8* %".17", i8* %".56", i8* null)
  %"x_counter" = alloca i32
  store i32 0, i32* %"x_counter"
  br label %"table_loop_start_x"
switch_case:
  %".48" = getelementptr [5 x i8], [5 x i8]* @".str.4", i32 0, i32 0
  %".49" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i8* %".48")
  br label %"switch_end"
switch_default:
  %".52" = getelementptr [6 x i8], [6 x i8]* @".str.5", i32 0, i32 0
  %".53" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i8* %".52")
  br label %"switch_end"
table_loop_start_x:
  %".60" = load i32, i32* %"x_counter"
  %".61" = icmp slt i32 %".60", 5
  br i1 %".61", label %"table_loop_body_x", label %"table_loop_end_x"
table_loop_body_x:
  %".63" = alloca [32 x i8]
  %".64" = getelementptr [32 x i8], [32 x i8]* %".63", i32 0, i32 0
  %".65" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".66" = add i32 %".60", 1
  %".67" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".64", i8* %".65", i32 %".66")
  %".68" = call i8* @"strdup"(i8* %".64")
  store i8* %".68", i8** %"x"
  %".70" = load i8*, i8** %"i"
  %".71" = load i8*, i8** %"x"
  %".72" = getelementptr [2 x i8], [2 x i8]* @".str.7", i32 0, i32 0
  %".73" = call i8* @"strstr"(i8* %".71", i8* %".72")
  %".74" = icmp ne i8* %".73", null
  %".75" = alloca [32 x i8]
  %".76" = getelementptr [32 x i8], [32 x i8]* %".75", i32 0, i32 0
  %".77" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".78" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".76", i8* %".77", i32 2)
  %".79" = call i8* @"strdup"(i8* %".76")
  %".80" = call double @"atof"(i8* %".71")
  %".81" = call double @"atof"(i8* %".79")
  %".82" = call double @"fmod"(double %".80", double %".81")
  %".83" = alloca [32 x i8]
  %".84" = getelementptr [32 x i8], [32 x i8]* %".83", i32 0, i32 0
  %".85" = getelementptr [5 x i8], [5 x i8]* @".str.8", i32 0, i32 0
  %".86" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".84", i8* %".85", double %".82")
  %".87" = call i8* @"strdup"(i8* %".84")
  %".88" = call i32 @"atoi"(i8* %".87")
  %".89" = icmp eq i32 %".88", 0
  br i1 %".89", label %"if_then", label %"if_else"
table_loop_end_x:
  %".108" = load i8*, i8** %"i"
  %".109" = load i8*, i8** %"x"
  %".110" = alloca [32 x i8]
  %".111" = getelementptr [32 x i8], [32 x i8]* %".110", i32 0, i32 0
  %".112" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".113" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".111", i8* %".112", i32 3)
  %".114" = call i8* @"strdup"(i8* %".111")
  %"counter" = alloca i8*
  store i8* %".114", i8** %"counter"
  br label %"while_cond"
if_then:
  %".91" = getelementptr [6 x i8], [6 x i8]* @".str.9", i32 0, i32 0
  %".92" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".93" = call i32 (i8*, ...) @"printf"(i8* %".92", i8* %".91")
  %".94" = load i8*, i8** %"x"
  %".95" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".96" = call i32 (i8*, ...) @"printf"(i8* %".95", i8* %".94")
  br label %"if_merge"
if_else:
  %".98" = getelementptr [5 x i8], [5 x i8]* @".str.10", i32 0, i32 0
  %".99" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".99", i8* %".98")
  %".101" = load i8*, i8** %"x"
  %".102" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".103" = call i32 (i8*, ...) @"printf"(i8* %".102", i8* %".101")
  br label %"if_merge"
if_merge:
  %".105" = add i32 %".60", 1
  store i32 %".105", i32* %"x_counter"
  br label %"table_loop_start_x"
while_cond:
  %".117" = load i8*, i8** %"counter"
  %".118" = call i32 @"atoi"(i8* %".117")
  %".119" = icmp sgt i32 %".118", 0
  br i1 %".119", label %"while_body", label %"while_end"
while_body:
  %".121" = load i8*, i8** %"counter"
  %".122" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".123" = call i32 (i8*, ...) @"printf"(i8* %".122", i8* %".121")
  %".124" = load i8*, i8** %"i"
  %".125" = load i8*, i8** %"x"
  %".126" = load i8*, i8** %"counter"
  %".127" = getelementptr [2 x i8], [2 x i8]* @".str.7", i32 0, i32 0
  %".128" = call i8* @"strstr"(i8* %".126", i8* %".127")
  %".129" = icmp ne i8* %".128", null
  %".130" = alloca [32 x i8]
  %".131" = getelementptr [32 x i8], [32 x i8]* %".130", i32 0, i32 0
  %".132" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".133" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".131", i8* %".132", i32 1)
  %".134" = call i8* @"strdup"(i8* %".131")
  %".135" = call double @"atof"(i8* %".126")
  %".136" = call double @"atof"(i8* %".134")
  %".137" = fsub double %".135", %".136"
  %".138" = alloca [32 x i8]
  %".139" = getelementptr [32 x i8], [32 x i8]* %".138", i32 0, i32 0
  %".140" = getelementptr [5 x i8], [5 x i8]* @".str.8", i32 0, i32 0
  %".141" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".139", i8* %".140", double %".137")
  %".142" = call i8* @"strdup"(i8* %".139")
  store i8* %".142", i8** %"counter"
  %".144" = sub i32 %".118", 1
  %".145" = alloca [32 x i8]
  %".146" = getelementptr [32 x i8], [32 x i8]* %".145", i32 0, i32 0
  %".147" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".148" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".146", i8* %".147", i32 %".144")
  %".149" = call i8* @"strdup"(i8* %".146")
  store i8* %".149", i8** %"counter"
  br label %"while_cond"
while_end:
  %".152" = getelementptr [2 x i8], [2 x i8]* @".str.11", i32 0, i32 0
  %".153" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".154" = call i32 (i8*, ...) @"printf"(i8* %".153", i8* %".152")
  %".155" = load i8*, i8** %"i"
  %".156" = load i8*, i8** %"x"
  %".157" = load i8*, i8** %"counter"
  %".158" = alloca [32 x i8]
  %".159" = getelementptr [32 x i8], [32 x i8]* %".158", i32 0, i32 0
  %".160" = getelementptr [5 x i8], [5 x i8]* @".str.8", i32 0, i32 0
  %".161" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".159", i8* %".160", double 0x3fb999999999999a)
  %".162" = call i8* @"strdup"(i8* %".159")
  store i8* %".162", i8** %"x"
  %".164" = load i8*, i8** %"i"
  %".165" = load i8*, i8** %"x"
  %".166" = load i8*, i8** %"counter"
  %".167" = alloca [32 x i8]
  %".168" = getelementptr [32 x i8], [32 x i8]* %".167", i32 0, i32 0
  %".169" = getelementptr [3 x i8], [3 x i8]* @".str.3", i32 0, i32 0
  %".170" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".168", i8* %".169", i32 4)
  %".171" = call i8* @"strdup"(i8* %".168")
  %"y" = alloca i8*
  store i8* %".171", i8** %"y"
  %".173" = load i8*, i8** %"i"
  %".174" = load i8*, i8** %"x"
  %".175" = load i8*, i8** %"counter"
  %".176" = load i8*, i8** %"y"
  %".177" = getelementptr [2 x i8], [2 x i8]* @".str.7", i32 0, i32 0
  %".178" = call i8* @"strstr"(i8* %".174", i8* %".177")
  %".179" = icmp ne i8* %".178", null
  %".180" = getelementptr [2 x i8], [2 x i8]* @".str.7", i32 0, i32 0
  %".181" = call i8* @"strstr"(i8* %".176", i8* %".180")
  %".182" = icmp ne i8* %".181", null
  %".183" = call double @"atof"(i8* %".174")
  %".184" = call double @"atof"(i8* %".176")
  %".185" = fadd double %".183", %".184"
  %".186" = alloca [32 x i8]
  %".187" = getelementptr [32 x i8], [32 x i8]* %".186", i32 0, i32 0
  %".188" = getelementptr [5 x i8], [5 x i8]* @".str.8", i32 0, i32 0
  %".189" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".187", i8* %".188", double %".185")
  %".190" = call i8* @"strdup"(i8* %".187")
  %"z" = alloca i8*
  store i8* %".190", i8** %"z"
  %".192" = load i8*, i8** %"z"
  %".193" = getelementptr [4 x i8], [4 x i8]* @".str.6", i32 0, i32 0
  %".194" = call i32 (i8*, ...) @"printf"(i8* %".193", i8* %".192")
  call void @"cleanup_all_tables"()
  ret i32 0
}

@".str.0" = internal constant [2 x i8] c"n\00", align 1
@".str.1" = internal constant [4 x i8] c"int\00", align 1
@".str.2" = internal constant [8 x i8] c"numbers\00", align 1
@".str.3" = internal constant [3 x i8] c"%d\00", align 1
@".str.4" = internal constant [5 x i8] c"true\00", align 1
@".str.5" = internal constant [6 x i8] c"false\00", align 1
@".str.6" = internal constant [4 x i8] c"%s\0a\00", align 1
@".str.7" = internal constant [2 x i8] c".\00", align 1
@".str.8" = internal constant [5 x i8] c"%.6f\00", align 1
@".str.9" = internal constant [6 x i8] c"even:\00", align 1
@".str.10" = internal constant [5 x i8] c"odd:\00", align 1
@".str.11" = internal constant [2 x i8] c" \00", align 1