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

declare i32 @"table_row_count"(i8* %".1")

declare i32 @"table_col_count"(i8* %".1")

declare i8* @"table_get_value"(i8* %".1", i32 %".2", i8* %".3")

declare void @"cleanup_all_tables"()

define i32 @"main"()
{
entry:
  %".2" = alloca [4 x i8*]
  %".3" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".4" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 0
  store i8* %".3", i8** %".4"
  %".6" = getelementptr [7 x i8], [7 x i8]* @".str.1", i32 0, i32 0
  %".7" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 1
  store i8* %".6", i8** %".7"
  %".9" = getelementptr [4 x i8], [4 x i8]* @".str.2", i32 0, i32 0
  %".10" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 2
  store i8* %".9", i8** %".10"
  %".12" = getelementptr [6 x i8], [6 x i8]* @".str.3", i32 0, i32 0
  %".13" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 3
  store i8* %".12", i8** %".13"
  %".15" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 0
  %".16" = alloca [4 x i8*]
  %".17" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".18" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 0
  store i8* %".17", i8** %".18"
  %".20" = getelementptr [6 x i8], [6 x i8]* @".str.5", i32 0, i32 0
  %".21" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 1
  store i8* %".20", i8** %".21"
  %".23" = getelementptr [6 x i8], [6 x i8]* @".str.5", i32 0, i32 0
  %".24" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 2
  store i8* %".23", i8** %".24"
  %".26" = getelementptr [6 x i8], [6 x i8]* @".str.5", i32 0, i32 0
  %".27" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 3
  store i8* %".26", i8** %".27"
  %".29" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 0
  %".30" = alloca [4 x i8*]
  %".31" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 0
  store i8* null, i8** %".31"
  %".33" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 1
  store i8* null, i8** %".33"
  %".35" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 2
  %".36" = getelementptr [13 x i8], [13 x i8]* @".str.6", i32 0, i32 0
  store i8* %".36", i8** %".35"
  %".38" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 3
  %".39" = getelementptr [13 x i8], [13 x i8]* @".str.7", i32 0, i32 0
  store i8* %".39", i8** %".38"
  %".41" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 0
  %".42" = getelementptr [13 x i8], [13 x i8]* @".str.8", i32 0, i32 0
  %".43" = call i8* @"create_table"(i8* %".42", i32 4, i8** %".15", i8** %".29", i8** %".41")
  %".44" = alloca [32 x i8]
  %".45" = getelementptr [32 x i8], [32 x i8]* %".44", i32 0, i32 0
  %".46" = getelementptr [3 x i8], [3 x i8]* @".str.9", i32 0, i32 0
  %".47" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".45", i8* %".46", i32 1)
  %".48" = call i8* @"strdup"(i8* %".45")
  %".49" = alloca [32 x i8]
  %".50" = getelementptr [32 x i8], [32 x i8]* %".49", i32 0, i32 0
  %".51" = getelementptr [5 x i8], [5 x i8]* @".str.10", i32 0, i32 0
  %".52" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".50", i8* %".51", double 0x4062c00000000000)
  %".53" = call i8* @"strdup"(i8* %".50")
  %".54" = alloca [4 x i8*]
  %".55" = getelementptr [4 x i8*], [4 x i8*]* %".54", i32 0, i32 0
  store i8* %".48", i8** %".55"
  %".57" = getelementptr [4 x i8*], [4 x i8*]* %".54", i32 0, i32 1
  store i8* %".53", i8** %".57"
  %".59" = getelementptr [4 x i8*], [4 x i8*]* %".54", i32 0, i32 2
  store i8* null, i8** %".59"
  %".61" = getelementptr [4 x i8*], [4 x i8*]* %".54", i32 0, i32 3
  store i8* null, i8** %".61"
  %".63" = getelementptr [4 x i8*], [4 x i8*]* %".54", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".43", i8** %".63")
  %".65" = alloca [32 x i8]
  %".66" = getelementptr [32 x i8], [32 x i8]* %".65", i32 0, i32 0
  %".67" = getelementptr [3 x i8], [3 x i8]* @".str.9", i32 0, i32 0
  %".68" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".66", i8* %".67", i32 2)
  %".69" = call i8* @"strdup"(i8* %".66")
  %".70" = alloca [32 x i8]
  %".71" = getelementptr [32 x i8], [32 x i8]* %".70", i32 0, i32 0
  %".72" = getelementptr [5 x i8], [5 x i8]* @".str.10", i32 0, i32 0
  %".73" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".71", i8* %".72", double 0x4054000000000000)
  %".74" = call i8* @"strdup"(i8* %".71")
  %".75" = alloca [4 x i8*]
  %".76" = getelementptr [4 x i8*], [4 x i8*]* %".75", i32 0, i32 0
  store i8* %".69", i8** %".76"
  %".78" = getelementptr [4 x i8*], [4 x i8*]* %".75", i32 0, i32 1
  store i8* %".74", i8** %".78"
  %".80" = getelementptr [4 x i8*], [4 x i8*]* %".75", i32 0, i32 2
  store i8* null, i8** %".80"
  %".82" = getelementptr [4 x i8*], [4 x i8*]* %".75", i32 0, i32 3
  store i8* null, i8** %".82"
  %".84" = getelementptr [4 x i8*], [4 x i8*]* %".75", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".43", i8** %".84")
  %".86" = getelementptr [20 x i8], [20 x i8]* @".str.11", i32 0, i32 0
  %"update transactions set amount" = alloca i8*
  store i8* %".86", i8** %"update transactions set amount"
  call void @"table_print"(i8* %".43")
  call void @"cleanup_all_tables"()
  ret i32 0
}

@".str.0" = internal constant [3 x i8] c"id\00", align 1
@".str.1" = internal constant [7 x i8] c"amount\00", align 1
@".str.2" = internal constant [4 x i8] c"tax\00", align 1
@".str.3" = internal constant [6 x i8] c"total\00", align 1
@".str.4" = internal constant [4 x i8] c"int\00", align 1
@".str.5" = internal constant [6 x i8] c"float\00", align 1
@".str.6" = internal constant [13 x i8] c"amount * 0.2\00", align 1
@".str.7" = internal constant [13 x i8] c"amount + tax\00", align 1
@".str.8" = internal constant [13 x i8] c"transactions\00", align 1
@".str.9" = internal constant [3 x i8] c"%d\00", align 1
@".str.10" = internal constant [5 x i8] c"%.2f\00", align 1
@".str.11" = internal constant [20 x i8] c"200.0 where id == 1\00", align 1