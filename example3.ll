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

declare void @"cleanup_all_tables"()

define i8* @"test_primer"(i8* %"n")
{
entry:
  %"n.1" = alloca i8*
  store i8* %"n", i8** %"n.1"
  %".4" = load i8*, i8** %"n.1"
  %".5" = call i32 @"atoi"(i8* %".4")
  %".6" = mul i32 3, %".5"
  %".7" = alloca [32 x i8]
  %".8" = getelementptr [32 x i8], [32 x i8]* %".7", i32 0, i32 0
  %".9" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".10" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".8", i8* %".9", i32 %".6")
  %".11" = call i8* @"strdup"(i8* %".8")
  %"z" = alloca i8*
  store i8* %".11", i8** %"z"
  %".13" = load i8*, i8** %"z"
  ret i8* %".13"
}

@".str.0" = internal constant [3 x i8] c"%d\00", align 1
define i8* @"is_prime"(i8* %"x")
{
entry:
  %"x.1" = alloca i8*
  store i8* %"x", i8** %"x.1"
  %".4" = load i8*, i8** %"x.1"
  %".5" = call i32 @"atoi"(i8* %".4")
  %".6" = icmp sle i32 %".5", 1
  br i1 %".6", label %"if_then", label %"if_merge"
if_then:
  %".8" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".9" = getelementptr [6 x i8], [6 x i8]* @".str.2", i32 0, i32 0
  %".10" = select  i1 false, i8* %".8", i8* %".9"
  ret i8* %".10"
if_merge:
  %".12" = load i8*, i8** %"x.1"
  %".13" = alloca [32 x i8]
  %".14" = getelementptr [32 x i8], [32 x i8]* %".13", i32 0, i32 0
  %".15" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".16" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".14", i8* %".15", i32 2)
  %".17" = call i8* @"strdup"(i8* %".14")
  %".18" = call i8* @"has_divisor"(i8* %".12", i8* %".17")
  %".19" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".20" = call i32 @"strcmp"(i8* %".18", i8* %".19")
  %".21" = icmp eq i32 %".20", 0
  %".22" = xor i1 %".21", -1
  %".23" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".24" = getelementptr [6 x i8], [6 x i8]* @".str.2", i32 0, i32 0
  %".25" = select  i1 %".22", i8* %".23", i8* %".24"
  ret i8* %".25"
}

@".str.1" = internal constant [5 x i8] c"true\00", align 1
@".str.2" = internal constant [6 x i8] c"false\00", align 1
define i8* @"has_divisor"(i8* %"y", i8* %"d")
{
entry:
  %"y.1" = alloca i8*
  store i8* %"y", i8** %"y.1"
  %"d.1" = alloca i8*
  store i8* %"d", i8** %"d.1"
  %".6" = load i8*, i8** %"y.1"
  %".7" = call i32 @"atoi"(i8* %".6")
  %".8" = icmp sgt i32 0, %".7"
  br i1 %".8", label %"if_then", label %"if_merge"
if_then:
  %".10" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".11" = getelementptr [6 x i8], [6 x i8]* @".str.2", i32 0, i32 0
  %".12" = select  i1 false, i8* %".10", i8* %".11"
  ret i8* %".12"
if_merge:
  %".14" = icmp eq i32 0, 0
  br i1 %".14", label %"if_then.1", label %"if_merge.1"
if_then.1:
  %".16" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".17" = getelementptr [6 x i8], [6 x i8]* @".str.2", i32 0, i32 0
  %".18" = select  i1 true, i8* %".16", i8* %".17"
  ret i8* %".18"
if_merge.1:
  %".20" = load i8*, i8** %"y.1"
  %".21" = getelementptr [6 x i8], [6 x i8]* @".str.3", i32 0, i32 0
  %".22" = call i8* @"has_divisor"(i8* %".20", i8* %".21")
  ret i8* %".22"
}

@".str.3" = internal constant [6 x i8] c"d + 1\00", align 1
define i8* @"is_prime_2"(i8* %"x", i8* %"has_divisor")
{
entry:
  %"x.1" = alloca i8*
  store i8* %"x", i8** %"x.1"
  %"has_divisor.1" = alloca i8*
  store i8* %"has_divisor", i8** %"has_divisor.1"
  %".6" = load i8*, i8** %"has_divisor.1"
  %".7" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".8" = call i32 @"strcmp"(i8* %".6", i8* %".7")
  %".9" = icmp eq i32 %".8", 0
  %".10" = xor i1 %".9", -1
  %".11" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".12" = getelementptr [6 x i8], [6 x i8]* @".str.2", i32 0, i32 0
  %".13" = select  i1 %".10", i8* %".11", i8* %".12"
  ret i8* %".13"
}

define i32 @"main"()
{
entry:
  %".2" = alloca [32 x i8]
  %".3" = getelementptr [32 x i8], [32 x i8]* %".2", i32 0, i32 0
  %".4" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".5" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".3", i8* %".4", i32 5)
  %".6" = call i8* @"strdup"(i8* %".3")
  %".7" = call i8* @"test_primer"(i8* %".6")
  %".8" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8* %".7")
  %".10" = alloca [32 x i8]
  %".11" = getelementptr [32 x i8], [32 x i8]* %".10", i32 0, i32 0
  %".12" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".13" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".11", i8* %".12", i32 7)
  %".14" = call i8* @"strdup"(i8* %".11")
  %".15" = call i8* @"is_prime"(i8* %".14")
  %".16" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i8* %".15")
  %".18" = alloca [32 x i8]
  %".19" = getelementptr [32 x i8], [32 x i8]* %".18", i32 0, i32 0
  %".20" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".21" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".19", i8* %".20", i32 9)
  %".22" = call i8* @"strdup"(i8* %".19")
  %".23" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".24" = call i8* @"is_prime_2"(i8* %".22", i8* %".23")
  %".25" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", i8* %".24")
  call void @"cleanup_all_tables"()
  ret i32 0
}

@".str.4" = internal constant [4 x i8] c"%s\0a\00", align 1