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
  %".6" = getelementptr [5 x i8], [5 x i8]* @".str.1", i32 0, i32 0
  %".7" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 1
  store i8* %".6", i8** %".7"
  %".9" = getelementptr [4 x i8], [4 x i8]* @".str.2", i32 0, i32 0
  %".10" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 2
  store i8* %".9", i8** %".10"
  %".12" = getelementptr [5 x i8], [5 x i8]* @".str.3", i32 0, i32 0
  %".13" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 3
  store i8* %".12", i8** %".13"
  %".15" = getelementptr [4 x i8*], [4 x i8*]* %".2", i32 0, i32 0
  %".16" = alloca [4 x i8*]
  %".17" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".18" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 0
  store i8* %".17", i8** %".18"
  %".20" = getelementptr [7 x i8], [7 x i8]* @".str.5", i32 0, i32 0
  %".21" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 1
  store i8* %".20", i8** %".21"
  %".23" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".24" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 2
  store i8* %".23", i8** %".24"
  %".26" = getelementptr [7 x i8], [7 x i8]* @".str.5", i32 0, i32 0
  %".27" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 3
  store i8* %".26", i8** %".27"
  %".29" = getelementptr [4 x i8*], [4 x i8*]* %".16", i32 0, i32 0
  %".30" = alloca [4 x i8*]
  %".31" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 0
  store i8* null, i8** %".31"
  %".33" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 1
  store i8* null, i8** %".33"
  %".35" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 2
  store i8* null, i8** %".35"
  %".37" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 3
  store i8* null, i8** %".37"
  %".39" = getelementptr [4 x i8*], [4 x i8*]* %".30", i32 0, i32 0
  %".40" = getelementptr [12 x i8], [12 x i8]* @".str.6", i32 0, i32 0
  %".41" = call i8* @"create_table"(i8* %".40", i32 4, i8** %".15", i8** %".29", i8** %".39")
  %".42" = alloca [4 x i8*]
  %".43" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".44" = getelementptr [4 x i8*], [4 x i8*]* %".42", i32 0, i32 0
  store i8* %".43", i8** %".44"
  %".46" = getelementptr [8 x i8], [8 x i8]* @".str.7", i32 0, i32 0
  %".47" = getelementptr [4 x i8*], [4 x i8*]* %".42", i32 0, i32 1
  store i8* %".46", i8** %".47"
  %".49" = getelementptr [7 x i8], [7 x i8]* @".str.8", i32 0, i32 0
  %".50" = getelementptr [4 x i8*], [4 x i8*]* %".42", i32 0, i32 2
  store i8* %".49", i8** %".50"
  %".52" = getelementptr [8 x i8], [8 x i8]* @".str.9", i32 0, i32 0
  %".53" = getelementptr [4 x i8*], [4 x i8*]* %".42", i32 0, i32 3
  store i8* %".52", i8** %".53"
  %".55" = getelementptr [4 x i8*], [4 x i8*]* %".42", i32 0, i32 0
  %".56" = alloca [4 x i8*]
  %".57" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".58" = getelementptr [4 x i8*], [4 x i8*]* %".56", i32 0, i32 0
  store i8* %".57", i8** %".58"
  %".60" = getelementptr [4 x i8], [4 x i8]* @".str.4", i32 0, i32 0
  %".61" = getelementptr [4 x i8*], [4 x i8*]* %".56", i32 0, i32 1
  store i8* %".60", i8** %".61"
  %".63" = getelementptr [6 x i8], [6 x i8]* @".str.10", i32 0, i32 0
  %".64" = getelementptr [4 x i8*], [4 x i8*]* %".56", i32 0, i32 2
  store i8* %".63", i8** %".64"
  %".66" = getelementptr [5 x i8], [5 x i8]* @".str.11", i32 0, i32 0
  %".67" = getelementptr [4 x i8*], [4 x i8*]* %".56", i32 0, i32 3
  store i8* %".66", i8** %".67"
  %".69" = getelementptr [4 x i8*], [4 x i8*]* %".56", i32 0, i32 0
  %".70" = alloca [4 x i8*]
  %".71" = getelementptr [4 x i8*], [4 x i8*]* %".70", i32 0, i32 0
  store i8* null, i8** %".71"
  %".73" = getelementptr [4 x i8*], [4 x i8*]* %".70", i32 0, i32 1
  store i8* null, i8** %".73"
  %".75" = getelementptr [4 x i8*], [4 x i8*]* %".70", i32 0, i32 2
  store i8* null, i8** %".75"
  %".77" = getelementptr [4 x i8*], [4 x i8*]* %".70", i32 0, i32 3
  store i8* null, i8** %".77"
  %".79" = getelementptr [4 x i8*], [4 x i8*]* %".70", i32 0, i32 0
  %".80" = getelementptr [13 x i8], [13 x i8]* @".str.12", i32 0, i32 0
  %".81" = call i8* @"create_table"(i8* %".80", i32 4, i8** %".55", i8** %".69", i8** %".79")
  %".82" = alloca [32 x i8]
  %".83" = getelementptr [32 x i8], [32 x i8]* %".82", i32 0, i32 0
  %".84" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".85" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".83", i8* %".84", i32 1)
  %".86" = call i8* @"strdup"(i8* %".83")
  %".87" = getelementptr [5 x i8], [5 x i8]* @".str.14", i32 0, i32 0
  %".88" = alloca [32 x i8]
  %".89" = getelementptr [32 x i8], [32 x i8]* %".88", i32 0, i32 0
  %".90" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".91" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".89", i8* %".90", i32 28)
  %".92" = call i8* @"strdup"(i8* %".89")
  %".93" = getelementptr [5 x i8], [5 x i8]* @".str.15", i32 0, i32 0
  %".94" = alloca [4 x i8*]
  %".95" = getelementptr [4 x i8*], [4 x i8*]* %".94", i32 0, i32 0
  store i8* %".86", i8** %".95"
  %".97" = getelementptr [4 x i8*], [4 x i8*]* %".94", i32 0, i32 1
  store i8* %".87", i8** %".97"
  %".99" = getelementptr [4 x i8*], [4 x i8*]* %".94", i32 0, i32 2
  store i8* %".92", i8** %".99"
  %".101" = getelementptr [4 x i8*], [4 x i8*]* %".94", i32 0, i32 3
  store i8* %".93", i8** %".101"
  %".103" = getelementptr [4 x i8*], [4 x i8*]* %".94", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".41", i8** %".103")
  %".105" = alloca [32 x i8]
  %".106" = getelementptr [32 x i8], [32 x i8]* %".105", i32 0, i32 0
  %".107" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".108" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".106", i8* %".107", i32 2)
  %".109" = call i8* @"strdup"(i8* %".106")
  %".110" = getelementptr [4 x i8], [4 x i8]* @".str.16", i32 0, i32 0
  %".111" = alloca [32 x i8]
  %".112" = getelementptr [32 x i8], [32 x i8]* %".111", i32 0, i32 0
  %".113" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".114" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".112", i8* %".113", i32 35)
  %".115" = call i8* @"strdup"(i8* %".112")
  %".116" = getelementptr [7 x i8], [7 x i8]* @".str.17", i32 0, i32 0
  %".117" = alloca [4 x i8*]
  %".118" = getelementptr [4 x i8*], [4 x i8*]* %".117", i32 0, i32 0
  store i8* %".109", i8** %".118"
  %".120" = getelementptr [4 x i8*], [4 x i8*]* %".117", i32 0, i32 1
  store i8* %".110", i8** %".120"
  %".122" = getelementptr [4 x i8*], [4 x i8*]* %".117", i32 0, i32 2
  store i8* %".115", i8** %".122"
  %".124" = getelementptr [4 x i8*], [4 x i8*]* %".117", i32 0, i32 3
  store i8* %".116", i8** %".124"
  %".126" = getelementptr [4 x i8*], [4 x i8*]* %".117", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".41", i8** %".126")
  call void @"table_print"(i8* %".41")
  %".129" = getelementptr [3 x i8], [3 x i8]* @".str.0", i32 0, i32 0
  %".130" = call i8* @"table_select"(i8* %".41", i8* %".129", i8* null)
  call void @"table_print"(i8* %".130")
  %".132" = call i32 @"table_row_count"(i8* %".130")
  %".133" = alloca [32 x i8]
  %".134" = getelementptr [32 x i8], [32 x i8]* %".133", i32 0, i32 0
  %".135" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".136" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".134", i8* %".135", i32 100)
  %".137" = call i8* @"strdup"(i8* %".134")
  %".138" = alloca [32 x i8]
  %".139" = getelementptr [32 x i8], [32 x i8]* %".138", i32 0, i32 0
  %".140" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".141" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".139", i8* %".140", i32 1)
  %".142" = call i8* @"strdup"(i8* %".139")
  %".143" = alloca [32 x i8]
  %".144" = getelementptr [32 x i8], [32 x i8]* %".143", i32 0, i32 0
  %".145" = getelementptr [5 x i8], [5 x i8]* @".str.18", i32 0, i32 0
  %".146" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".144", i8* %".145", double 0x4048f9999999999a)
  %".147" = call i8* @"strdup"(i8* %".144")
  %".148" = getelementptr [11 x i8], [11 x i8]* @".str.19", i32 0, i32 0
  %".149" = alloca [4 x i8*]
  %".150" = getelementptr [4 x i8*], [4 x i8*]* %".149", i32 0, i32 0
  store i8* %".137", i8** %".150"
  %".152" = getelementptr [4 x i8*], [4 x i8*]* %".149", i32 0, i32 1
  store i8* %".142", i8** %".152"
  %".154" = getelementptr [4 x i8*], [4 x i8*]* %".149", i32 0, i32 2
  store i8* %".147", i8** %".154"
  %".156" = getelementptr [4 x i8*], [4 x i8*]* %".149", i32 0, i32 3
  store i8* %".148", i8** %".156"
  %".158" = getelementptr [4 x i8*], [4 x i8*]* %".149", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".81", i8** %".158")
  %".160" = alloca [32 x i8]
  %".161" = getelementptr [32 x i8], [32 x i8]* %".160", i32 0, i32 0
  %".162" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".163" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".161", i8* %".162", i32 101)
  %".164" = call i8* @"strdup"(i8* %".161")
  %".165" = alloca [32 x i8]
  %".166" = getelementptr [32 x i8], [32 x i8]* %".165", i32 0, i32 0
  %".167" = getelementptr [3 x i8], [3 x i8]* @".str.13", i32 0, i32 0
  %".168" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".166", i8* %".167", i32 2)
  %".169" = call i8* @"strdup"(i8* %".166")
  %".170" = alloca [32 x i8]
  %".171" = getelementptr [32 x i8], [32 x i8]* %".170", i32 0, i32 0
  %".172" = getelementptr [5 x i8], [5 x i8]* @".str.18", i32 0, i32 0
  %".173" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".171", i8* %".172", double 0x4033fd70a3d70a3d)
  %".174" = call i8* @"strdup"(i8* %".171")
  %".175" = getelementptr [11 x i8], [11 x i8]* @".str.20", i32 0, i32 0
  %".176" = alloca [4 x i8*]
  %".177" = getelementptr [4 x i8*], [4 x i8*]* %".176", i32 0, i32 0
  store i8* %".164", i8** %".177"
  %".179" = getelementptr [4 x i8*], [4 x i8*]* %".176", i32 0, i32 1
  store i8* %".169", i8** %".179"
  %".181" = getelementptr [4 x i8*], [4 x i8*]* %".176", i32 0, i32 2
  store i8* %".174", i8** %".181"
  %".183" = getelementptr [4 x i8*], [4 x i8*]* %".176", i32 0, i32 3
  store i8* %".175", i8** %".183"
  %".185" = getelementptr [4 x i8*], [4 x i8*]* %".176", i32 0, i32 0
  call void @"table_insert_silent"(i8* %".81", i8** %".185")
  %".187" = getelementptr [36 x i8], [36 x i8]* @".str.21", i32 0, i32 0
  %".188" = call i8* @"table_join"(i8* %".41", i8* %".81", i8* %".187")
  %".189" = getelementptr [61 x i8], [61 x i8]* @".str.22", i32 0, i32 0
  %".190" = call i8* @"table_filter"(i8* %".188", i8* %".189")
  %".191" = getelementptr [7 x i8], [7 x i8]* @".str.8", i32 0, i32 0
  %".192" = call i8* @"table_sort"(i8* %".190", i8* %".191", i32 1)
  call void @"table_print"(i8* %".192")
  call void @"cleanup_all_tables"()
  ret i32 0
}

@".str.0" = internal constant [3 x i8] c"id\00", align 1
@".str.1" = internal constant [5 x i8] c"name\00", align 1
@".str.2" = internal constant [4 x i8] c"age\00", align 1
@".str.3" = internal constant [5 x i8] c"city\00", align 1
@".str.4" = internal constant [4 x i8] c"int\00", align 1
@".str.5" = internal constant [7 x i8] c"string\00", align 1
@".str.6" = internal constant [12 x i8] c"users_table\00", align 1
@".str.7" = internal constant [8 x i8] c"user_id\00", align 1
@".str.8" = internal constant [7 x i8] c"amount\00", align 1
@".str.9" = internal constant [8 x i8] c"created\00", align 1
@".str.10" = internal constant [6 x i8] c"float\00", align 1
@".str.11" = internal constant [5 x i8] c"date\00", align 1
@".str.12" = internal constant [13 x i8] c"orders_table\00", align 1
@".str.13" = internal constant [3 x i8] c"%d\00", align 1
@".str.14" = internal constant [5 x i8] c"Anna\00", align 1
@".str.15" = internal constant [5 x i8] c"Oslo\00", align 1
@".str.16" = internal constant [4 x i8] c"Ola\00", align 1
@".str.17" = internal constant [7 x i8] c"Bergen\00", align 1
@".str.18" = internal constant [5 x i8] c"%.2f\00", align 1
@".str.19" = internal constant [11 x i8] c"2025-09-01\00", align 1
@".str.20" = internal constant [11 x i8] c"2025-09-03\00", align 1
@".str.21" = internal constant [36 x i8] c"users_table.id=orders_table.user_id\00", align 1
@".str.22" = internal constant [61 x i8] c"orders_table.amount > 10 and LEFT(users_table.name, 1) = 'A'\00", align 1