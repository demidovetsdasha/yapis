# Generated from ./DashSQLParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,467,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,5,0,80,
        8,0,10,0,12,0,83,9,0,1,0,1,0,1,1,1,1,3,1,89,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,102,8,2,1,3,1,3,1,3,1,3,1,3,3,3,
        109,8,3,1,4,1,4,1,4,1,4,3,4,115,8,4,1,4,1,4,1,4,4,4,120,8,4,11,4,
        12,4,121,1,5,1,5,1,5,5,5,127,8,5,10,5,12,5,130,9,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,143,8,7,1,8,1,8,1,8,5,8,148,8,
        8,10,8,12,8,151,9,8,1,9,1,9,1,9,5,9,156,8,9,10,9,12,9,159,9,9,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,5,
        12,174,8,12,10,12,12,12,177,9,12,1,13,1,13,1,13,1,13,1,13,3,13,184,
        8,13,1,13,1,13,1,13,1,13,1,13,1,13,4,13,192,8,13,11,13,12,13,193,
        3,13,196,8,13,1,14,1,14,1,15,1,15,1,15,1,15,3,15,204,8,15,1,15,1,
        15,4,15,208,8,15,11,15,12,15,209,1,16,1,16,1,16,1,16,1,16,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,227,8,18,10,18,12,
        18,230,9,18,1,18,1,18,3,18,234,8,18,1,19,1,19,1,19,1,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,3,20,247,8,20,1,21,1,21,1,21,1,21,1,21,
        3,21,254,8,21,1,21,1,21,3,21,258,8,21,1,22,1,22,1,22,1,22,5,22,264,
        8,22,10,22,12,22,267,9,22,3,22,269,8,22,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,284,8,24,1,25,1,25,
        1,25,1,25,1,25,1,25,3,25,292,8,25,1,26,1,26,1,26,1,26,3,26,298,8,
        26,1,26,1,26,1,26,1,26,1,26,3,26,305,8,26,1,26,1,26,1,26,1,26,1,
        26,1,26,3,26,313,8,26,3,26,315,8,26,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,4,27,325,8,27,11,27,12,27,326,1,27,1,27,1,27,1,27,1,27,
        1,27,4,27,335,8,27,11,27,12,27,336,3,27,339,8,27,1,28,1,28,1,28,
        1,28,4,28,345,8,28,11,28,12,28,346,1,29,1,29,1,29,1,29,4,29,353,
        8,29,11,29,12,29,354,1,29,1,29,1,29,4,29,360,8,29,11,29,12,29,361,
        3,29,364,8,29,1,30,1,30,1,30,1,30,1,30,4,30,371,8,30,11,30,12,30,
        372,1,31,1,31,1,31,1,31,1,31,4,31,380,8,31,11,31,12,31,381,1,31,
        1,31,1,31,1,31,4,31,388,8,31,11,31,12,31,389,3,31,392,8,31,1,32,
        1,32,1,32,4,32,397,8,32,11,32,12,32,398,1,33,1,33,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,413,8,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,5,34,427,8,34,10,34,
        12,34,430,9,34,1,35,1,35,1,35,1,35,1,35,1,35,3,35,438,8,35,1,36,
        1,36,1,36,3,36,443,8,36,1,36,1,36,1,37,1,37,1,38,1,38,1,38,5,38,
        452,8,38,10,38,12,38,455,9,38,1,38,1,38,1,38,5,38,460,8,38,10,38,
        12,38,463,9,38,3,38,465,8,38,1,38,0,1,68,39,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,0,5,1,0,31,35,1,0,41,46,1,0,37,38,2,0,39,
        40,48,48,1,0,56,60,494,0,81,1,0,0,0,2,88,1,0,0,0,4,101,1,0,0,0,6,
        108,1,0,0,0,8,110,1,0,0,0,10,123,1,0,0,0,12,131,1,0,0,0,14,142,1,
        0,0,0,16,144,1,0,0,0,18,152,1,0,0,0,20,160,1,0,0,0,22,163,1,0,0,
        0,24,170,1,0,0,0,26,195,1,0,0,0,28,197,1,0,0,0,30,199,1,0,0,0,32,
        211,1,0,0,0,34,216,1,0,0,0,36,220,1,0,0,0,38,235,1,0,0,0,40,246,
        1,0,0,0,42,248,1,0,0,0,44,268,1,0,0,0,46,270,1,0,0,0,48,273,1,0,
        0,0,50,285,1,0,0,0,52,314,1,0,0,0,54,338,1,0,0,0,56,340,1,0,0,0,
        58,348,1,0,0,0,60,365,1,0,0,0,62,391,1,0,0,0,64,393,1,0,0,0,66,400,
        1,0,0,0,68,412,1,0,0,0,70,437,1,0,0,0,72,439,1,0,0,0,74,446,1,0,
        0,0,76,464,1,0,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,0,81,
        79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,0,0,
        1,85,1,1,0,0,0,86,89,3,4,2,0,87,89,3,6,3,0,88,86,1,0,0,0,88,87,1,
        0,0,0,89,3,1,0,0,0,90,102,3,22,11,0,91,102,3,30,15,0,92,102,3,36,
        18,0,93,102,3,40,20,0,94,102,3,42,21,0,95,102,3,48,24,0,96,102,3,
        50,25,0,97,102,3,52,26,0,98,102,3,14,7,0,99,102,3,66,33,0,100,102,
        3,20,10,0,101,90,1,0,0,0,101,91,1,0,0,0,101,92,1,0,0,0,101,93,1,
        0,0,0,101,94,1,0,0,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,
        0,101,98,1,0,0,0,101,99,1,0,0,0,101,100,1,0,0,0,102,5,1,0,0,0,103,
        109,3,58,29,0,104,109,3,54,27,0,105,109,3,56,28,0,106,109,3,60,30,
        0,107,109,3,8,4,0,108,103,1,0,0,0,108,104,1,0,0,0,108,105,1,0,0,
        0,108,106,1,0,0,0,108,107,1,0,0,0,109,7,1,0,0,0,110,111,5,29,0,0,
        111,112,5,61,0,0,112,114,5,49,0,0,113,115,3,10,5,0,114,113,1,0,0,
        0,114,115,1,0,0,0,115,116,1,0,0,0,116,117,5,50,0,0,117,119,5,54,
        0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,
        0,0,121,122,1,0,0,0,122,9,1,0,0,0,123,128,3,12,6,0,124,125,5,53,
        0,0,125,127,3,12,6,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,
        0,0,128,129,1,0,0,0,129,11,1,0,0,0,130,128,1,0,0,0,131,132,5,61,
        0,0,132,133,5,54,0,0,133,134,3,28,14,0,134,13,1,0,0,0,135,136,5,
        61,0,0,136,137,5,55,0,0,137,143,3,68,34,0,138,139,3,16,8,0,139,140,
        5,55,0,0,140,141,3,18,9,0,141,143,1,0,0,0,142,135,1,0,0,0,142,138,
        1,0,0,0,143,15,1,0,0,0,144,149,5,61,0,0,145,146,5,53,0,0,146,148,
        5,61,0,0,147,145,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,17,1,0,0,0,151,149,1,0,0,0,152,157,3,68,34,0,153,154,
        5,53,0,0,154,156,3,68,34,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,19,1,0,0,0,159,157,1,0,0,0,160,161,5,
        30,0,0,161,162,3,68,34,0,162,21,1,0,0,0,163,164,5,2,0,0,164,165,
        5,61,0,0,165,166,5,3,0,0,166,167,5,49,0,0,167,168,3,24,12,0,168,
        169,5,50,0,0,169,23,1,0,0,0,170,175,3,26,13,0,171,172,5,53,0,0,172,
        174,3,26,13,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,
        176,1,0,0,0,176,25,1,0,0,0,177,175,1,0,0,0,178,179,5,61,0,0,179,
        180,5,54,0,0,180,183,3,28,14,0,181,182,5,55,0,0,182,184,3,68,34,
        0,183,181,1,0,0,0,183,184,1,0,0,0,184,196,1,0,0,0,185,186,5,61,0,
        0,186,187,5,54,0,0,187,188,3,28,14,0,188,189,5,55,0,0,189,191,5,
        54,0,0,190,192,3,2,1,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,1,
        0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,178,1,0,0,0,195,185,1,
        0,0,0,196,27,1,0,0,0,197,198,7,0,0,0,198,29,1,0,0,0,199,200,5,4,
        0,0,200,201,5,5,0,0,201,203,5,61,0,0,202,204,3,32,16,0,203,202,1,
        0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,207,5,54,0,0,206,208,3,
        34,17,0,207,206,1,0,0,0,208,209,1,0,0,0,209,207,1,0,0,0,209,210,
        1,0,0,0,210,31,1,0,0,0,211,212,5,6,0,0,212,213,5,61,0,0,213,214,
        5,7,0,0,214,215,5,61,0,0,215,33,1,0,0,0,216,217,3,16,8,0,217,218,
        5,55,0,0,218,219,3,18,9,0,219,35,1,0,0,0,220,221,5,18,0,0,221,222,
        5,61,0,0,222,223,5,19,0,0,223,228,3,38,19,0,224,225,5,53,0,0,225,
        227,3,38,19,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,
        229,1,0,0,0,229,233,1,0,0,0,230,228,1,0,0,0,231,232,5,6,0,0,232,
        234,3,76,38,0,233,231,1,0,0,0,233,234,1,0,0,0,234,37,1,0,0,0,235,
        236,5,61,0,0,236,237,5,55,0,0,237,238,3,68,34,0,238,39,1,0,0,0,239,
        240,5,8,0,0,240,247,3,68,34,0,241,242,5,8,0,0,242,243,5,49,0,0,243,
        244,3,68,34,0,244,245,5,50,0,0,245,247,1,0,0,0,246,239,1,0,0,0,246,
        241,1,0,0,0,247,41,1,0,0,0,248,249,5,9,0,0,249,250,3,44,22,0,250,
        251,5,7,0,0,251,253,5,61,0,0,252,254,3,46,23,0,253,252,1,0,0,0,253,
        254,1,0,0,0,254,257,1,0,0,0,255,256,5,10,0,0,256,258,5,61,0,0,257,
        255,1,0,0,0,257,258,1,0,0,0,258,43,1,0,0,0,259,269,5,48,0,0,260,
        265,5,61,0,0,261,262,5,53,0,0,262,264,5,61,0,0,263,261,1,0,0,0,264,
        267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,269,1,0,0,0,267,
        265,1,0,0,0,268,259,1,0,0,0,268,260,1,0,0,0,269,45,1,0,0,0,270,271,
        5,6,0,0,271,272,3,76,38,0,272,47,1,0,0,0,273,274,5,11,0,0,274,275,
        5,61,0,0,275,276,5,3,0,0,276,277,5,61,0,0,277,278,5,15,0,0,278,279,
        5,61,0,0,279,280,5,12,0,0,280,283,5,61,0,0,281,282,5,10,0,0,282,
        284,5,61,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,49,1,0,0,0,285,
        286,5,14,0,0,286,287,5,61,0,0,287,288,5,15,0,0,288,291,3,76,38,0,
        289,290,5,10,0,0,290,292,5,61,0,0,291,289,1,0,0,0,291,292,1,0,0,
        0,292,51,1,0,0,0,293,294,5,16,0,0,294,295,5,46,0,0,295,297,5,17,
        0,0,296,298,5,45,0,0,297,296,1,0,0,0,297,298,1,0,0,0,298,299,1,0,
        0,0,299,300,5,61,0,0,300,301,5,15,0,0,301,304,5,61,0,0,302,303,5,
        10,0,0,303,305,5,61,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,315,
        1,0,0,0,306,307,5,16,0,0,307,308,5,61,0,0,308,309,5,15,0,0,309,312,
        5,61,0,0,310,311,5,10,0,0,311,313,5,61,0,0,312,310,1,0,0,0,312,313,
        1,0,0,0,313,315,1,0,0,0,314,293,1,0,0,0,314,306,1,0,0,0,315,53,1,
        0,0,0,316,317,5,20,0,0,317,318,5,61,0,0,318,319,5,21,0,0,319,320,
        3,68,34,0,320,321,5,36,0,0,321,322,3,68,34,0,322,324,5,54,0,0,323,
        325,3,2,1,0,324,323,1,0,0,0,325,326,1,0,0,0,326,324,1,0,0,0,326,
        327,1,0,0,0,327,339,1,0,0,0,328,329,5,20,0,0,329,330,5,61,0,0,330,
        331,5,21,0,0,331,332,5,61,0,0,332,334,5,54,0,0,333,335,3,2,1,0,334,
        333,1,0,0,0,335,336,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,0,337,
        339,1,0,0,0,338,316,1,0,0,0,338,328,1,0,0,0,339,55,1,0,0,0,340,341,
        5,22,0,0,341,342,3,76,38,0,342,344,5,54,0,0,343,345,3,2,1,0,344,
        343,1,0,0,0,345,346,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,
        57,1,0,0,0,348,349,5,23,0,0,349,350,3,76,38,0,350,352,5,54,0,0,351,
        353,3,2,1,0,352,351,1,0,0,0,353,354,1,0,0,0,354,352,1,0,0,0,354,
        355,1,0,0,0,355,363,1,0,0,0,356,357,5,24,0,0,357,359,5,54,0,0,358,
        360,3,2,1,0,359,358,1,0,0,0,360,361,1,0,0,0,361,359,1,0,0,0,361,
        362,1,0,0,0,362,364,1,0,0,0,363,356,1,0,0,0,363,364,1,0,0,0,364,
        59,1,0,0,0,365,366,5,25,0,0,366,367,3,68,34,0,367,370,5,54,0,0,368,
        371,3,62,31,0,369,371,3,64,32,0,370,368,1,0,0,0,370,369,1,0,0,0,
        371,372,1,0,0,0,372,370,1,0,0,0,372,373,1,0,0,0,373,61,1,0,0,0,374,
        375,5,26,0,0,375,376,5,27,0,0,376,377,3,68,34,0,377,379,5,54,0,0,
        378,380,3,2,1,0,379,378,1,0,0,0,380,381,1,0,0,0,381,379,1,0,0,0,
        381,382,1,0,0,0,382,392,1,0,0,0,383,384,5,26,0,0,384,385,3,68,34,
        0,385,387,5,54,0,0,386,388,3,2,1,0,387,386,1,0,0,0,388,389,1,0,0,
        0,389,387,1,0,0,0,389,390,1,0,0,0,390,392,1,0,0,0,391,374,1,0,0,
        0,391,383,1,0,0,0,392,63,1,0,0,0,393,394,5,28,0,0,394,396,5,54,0,
        0,395,397,3,2,1,0,396,395,1,0,0,0,397,398,1,0,0,0,398,396,1,0,0,
        0,398,399,1,0,0,0,399,65,1,0,0,0,400,401,3,72,36,0,401,67,1,0,0,
        0,402,403,6,34,-1,0,403,404,5,47,0,0,404,413,3,68,34,4,405,406,5,
        61,0,0,406,407,5,51,0,0,407,408,3,68,34,0,408,409,5,52,0,0,409,413,
        1,0,0,0,410,413,3,72,36,0,411,413,3,70,35,0,412,402,1,0,0,0,412,
        405,1,0,0,0,412,410,1,0,0,0,412,411,1,0,0,0,413,428,1,0,0,0,414,
        415,10,8,0,0,415,416,5,27,0,0,416,427,3,68,34,9,417,418,10,7,0,0,
        418,419,7,1,0,0,419,427,3,68,34,8,420,421,10,6,0,0,421,422,7,2,0,
        0,422,427,3,68,34,7,423,424,10,5,0,0,424,425,7,3,0,0,425,427,3,68,
        34,6,426,414,1,0,0,0,426,417,1,0,0,0,426,420,1,0,0,0,426,423,1,0,
        0,0,427,430,1,0,0,0,428,426,1,0,0,0,428,429,1,0,0,0,429,69,1,0,0,
        0,430,428,1,0,0,0,431,432,5,49,0,0,432,433,3,68,34,0,433,434,5,50,
        0,0,434,438,1,0,0,0,435,438,3,74,37,0,436,438,5,61,0,0,437,431,1,
        0,0,0,437,435,1,0,0,0,437,436,1,0,0,0,438,71,1,0,0,0,439,440,5,61,
        0,0,440,442,5,49,0,0,441,443,3,18,9,0,442,441,1,0,0,0,442,443,1,
        0,0,0,443,444,1,0,0,0,444,445,5,50,0,0,445,73,1,0,0,0,446,447,7,
        4,0,0,447,75,1,0,0,0,448,453,3,68,34,0,449,450,5,12,0,0,450,452,
        3,68,34,0,451,449,1,0,0,0,452,455,1,0,0,0,453,451,1,0,0,0,453,454,
        1,0,0,0,454,465,1,0,0,0,455,453,1,0,0,0,456,461,3,68,34,0,457,458,
        5,13,0,0,458,460,3,68,34,0,459,457,1,0,0,0,460,463,1,0,0,0,461,459,
        1,0,0,0,461,462,1,0,0,0,462,465,1,0,0,0,463,461,1,0,0,0,464,448,
        1,0,0,0,464,456,1,0,0,0,465,77,1,0,0,0,50,81,88,101,108,114,121,
        128,142,149,157,175,183,193,195,203,209,228,233,246,253,257,265,
        268,283,291,297,304,312,314,326,336,338,346,354,361,363,370,372,
        381,389,391,398,412,426,428,437,442,453,461,464
    ]

class DashSQLParser ( Parser ):

    grammarFileName = "DashSQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'create'", "'with'", "'insert'", 
                     "'to'", "'where'", "'from'", "'write'", "'select'", 
                     "'as'", "'join'", "'and'", "'or'", "'filter'", "'by'", 
                     "'sort'", "'desc'", "'update'", "'set'", "'for'", "'in'", 
                     "'while'", "'if'", "'else'", "'switch'", "'case'", 
                     "'is'", "'default'", "'function'", "'return'", "'int'", 
                     "'string'", "'float'", "'date'", "'bool'", "'..'", 
                     "'+'", "'-'", "'/'", "'%'", "'=='", "'!='", "'>='", 
                     "'<='", "'>'", "'<'", "'not'", "'*'", "'('", "')'", 
                     "'['", "']'", "','", "':'", "'='", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "CREATE", "WITH", "INSERT", 
                      "TO", "WHERE", "FROM", "WRITE", "SELECT", "AS", "JOIN", 
                      "AND", "OR", "FILTER", "BY", "SORT", "DESC", "UPDATE", 
                      "SET", "FOR", "IN", "WHILE", "IF", "ELSE", "SWITCH", 
                      "CASE", "IS", "DEFAULT", "FUNCTION", "RETURN", "INT_TYPE", 
                      "STRING_TYPE", "FLOAT_TYPE", "DATE_TYPE", "BOOL_TYPE", 
                      "DOT2", "PLUS", "MINUS", "DIV", "MOD", "EQ", "NEQ", 
                      "GTE", "LTE", "GT", "LT", "NOT", "MULT", "LPAREN", 
                      "RPAREN", "LBRACKET", "RBRACKET", "COMMA", "COLON", 
                      "EQUALS", "TRUE_LIT", "FALSE_LIT", "INTEGER", "FLOAT_NUM", 
                      "STRING_LIT", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_simple_stmt = 2
    RULE_compound_stmt = 3
    RULE_function_def = 4
    RULE_param_list = 5
    RULE_param_def = 6
    RULE_assignment_stmt = 7
    RULE_id_list = 8
    RULE_expr_list = 9
    RULE_return_stmt = 10
    RULE_create_table_stmt = 11
    RULE_column_def_list = 12
    RULE_column_def = 13
    RULE_type_name = 14
    RULE_insert_stmt = 15
    RULE_where_from_condition = 16
    RULE_insert_row = 17
    RULE_update_stmt = 18
    RULE_update_assignment = 19
    RULE_write_stmt = 20
    RULE_select_stmt = 21
    RULE_column_list = 22
    RULE_where_condition = 23
    RULE_join_stmt = 24
    RULE_filter_stmt = 25
    RULE_sort_stmt = 26
    RULE_for_stmt = 27
    RULE_while_stmt = 28
    RULE_if_stmt = 29
    RULE_switch_stmt = 30
    RULE_case_stmt = 31
    RULE_default_stmt = 32
    RULE_function_call_stmt = 33
    RULE_expr = 34
    RULE_atom = 35
    RULE_function_call = 36
    RULE_literal_value = 37
    RULE_condition = 38

    ruleNames =  [ "program", "statement", "simple_stmt", "compound_stmt", 
                   "function_def", "param_list", "param_def", "assignment_stmt", 
                   "id_list", "expr_list", "return_stmt", "create_table_stmt", 
                   "column_def_list", "column_def", "type_name", "insert_stmt", 
                   "where_from_condition", "insert_row", "update_stmt", 
                   "update_assignment", "write_stmt", "select_stmt", "column_list", 
                   "where_condition", "join_stmt", "filter_stmt", "sort_stmt", 
                   "for_stmt", "while_stmt", "if_stmt", "switch_stmt", "case_stmt", 
                   "default_stmt", "function_call_stmt", "expr", "atom", 
                   "function_call", "literal_value", "condition" ]

    EOF = Token.EOF
    NEWLINE=1
    CREATE=2
    WITH=3
    INSERT=4
    TO=5
    WHERE=6
    FROM=7
    WRITE=8
    SELECT=9
    AS=10
    JOIN=11
    AND=12
    OR=13
    FILTER=14
    BY=15
    SORT=16
    DESC=17
    UPDATE=18
    SET=19
    FOR=20
    IN=21
    WHILE=22
    IF=23
    ELSE=24
    SWITCH=25
    CASE=26
    IS=27
    DEFAULT=28
    FUNCTION=29
    RETURN=30
    INT_TYPE=31
    STRING_TYPE=32
    FLOAT_TYPE=33
    DATE_TYPE=34
    BOOL_TYPE=35
    DOT2=36
    PLUS=37
    MINUS=38
    DIV=39
    MOD=40
    EQ=41
    NEQ=42
    GTE=43
    LTE=44
    GT=45
    LT=46
    NOT=47
    MULT=48
    LPAREN=49
    RPAREN=50
    LBRACKET=51
    RBRACKET=52
    COMMA=53
    COLON=54
    EQUALS=55
    TRUE_LIT=56
    FALSE_LIT=57
    INTEGER=58
    FLOAT_NUM=59
    STRING_LIT=60
    ID=61
    WS=62
    COMMENT=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DashSQLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DashSQLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2305843010871839508) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(DashSQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DashSQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4, 8, 9, 11, 14, 16, 18, 30, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.simple_stmt()
                pass
            elif token in [20, 22, 23, 25, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.compound_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_table_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Create_table_stmtContext,0)


        def insert_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Insert_stmtContext,0)


        def update_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Update_stmtContext,0)


        def write_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Write_stmtContext,0)


        def select_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Select_stmtContext,0)


        def join_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Join_stmtContext,0)


        def filter_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Filter_stmtContext,0)


        def sort_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Sort_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Assignment_stmtContext,0)


        def function_call_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Function_call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = DashSQLParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmt)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.create_table_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.insert_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.update_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.write_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.select_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 95
                self.join_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 96
                self.filter_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 97
                self.sort_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 98
                self.assignment_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 99
                self.function_call_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 100
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.While_stmtContext,0)


        def switch_stmt(self):
            return self.getTypedRuleContext(DashSQLParser.Switch_stmtContext,0)


        def function_def(self):
            return self.getTypedRuleContext(DashSQLParser.Function_defContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_compound_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stmt" ):
                listener.enterCompound_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stmt" ):
                listener.exitCompound_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_stmt" ):
                return visitor.visitCompound_stmt(self)
            else:
                return visitor.visitChildren(self)




    def compound_stmt(self):

        localctx = DashSQLParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compound_stmt)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.if_stmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.for_stmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.while_stmt()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.switch_stmt()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.function_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(DashSQLParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DashSQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DashSQLParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(DashSQLParser.Param_listContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = DashSQLParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(DashSQLParser.FUNCTION)
            self.state = 111
            self.match(DashSQLParser.ID)
            self.state = 112
            self.match(DashSQLParser.LPAREN)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==61:
                self.state = 113
                self.param_list()


            self.state = 116
            self.match(DashSQLParser.RPAREN)
            self.state = 117
            self.match(DashSQLParser.COLON)
            self.state = 119 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 118
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 121 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.Param_defContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.Param_defContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COMMA)
            else:
                return self.getToken(DashSQLParser.COMMA, i)

        def getRuleIndex(self):
            return DashSQLParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = DashSQLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.param_def()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 124
                self.match(DashSQLParser.COMMA)
                self.state = 125
                self.param_def()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(DashSQLParser.Type_nameContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_param_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_def" ):
                listener.enterParam_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_def" ):
                listener.exitParam_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def" ):
                return visitor.visitParam_def(self)
            else:
                return visitor.visitChildren(self)




    def param_def(self):

        localctx = DashSQLParser.Param_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(DashSQLParser.ID)
            self.state = 132
            self.match(DashSQLParser.COLON)
            self.state = 133
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DashSQLParser.RULE_assignment_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleAssignmentContext(Assignment_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.Assignment_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)
        def EQUALS(self):
            return self.getToken(DashSQLParser.EQUALS, 0)
        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssignment" ):
                listener.enterSimpleAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssignment" ):
                listener.exitSimpleAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleAssignment" ):
                return visitor.visitSimpleAssignment(self)
            else:
                return visitor.visitChildren(self)


    class MultiAssignmentContext(Assignment_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.Assignment_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_list(self):
            return self.getTypedRuleContext(DashSQLParser.Id_listContext,0)

        def EQUALS(self):
            return self.getToken(DashSQLParser.EQUALS, 0)
        def expr_list(self):
            return self.getTypedRuleContext(DashSQLParser.Expr_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiAssignment" ):
                listener.enterMultiAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiAssignment" ):
                listener.exitMultiAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiAssignment" ):
                return visitor.visitMultiAssignment(self)
            else:
                return visitor.visitChildren(self)



    def assignment_stmt(self):

        localctx = DashSQLParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment_stmt)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = DashSQLParser.SimpleAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(DashSQLParser.ID)
                self.state = 136
                self.match(DashSQLParser.EQUALS)
                self.state = 137
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = DashSQLParser.MultiAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.id_list()
                self.state = 139
                self.match(DashSQLParser.EQUALS)
                self.state = 140
                self.expr_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COMMA)
            else:
                return self.getToken(DashSQLParser.COMMA, i)

        def getRuleIndex(self):
            return DashSQLParser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = DashSQLParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(DashSQLParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 145
                self.match(DashSQLParser.COMMA)
                self.state = 146
                self.match(DashSQLParser.ID)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COMMA)
            else:
                return self.getToken(DashSQLParser.COMMA, i)

        def getRuleIndex(self):
            return DashSQLParser.RULE_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_list" ):
                listener.enterExpr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_list" ):
                listener.exitExpr_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = DashSQLParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.expr(0)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self.match(DashSQLParser.COMMA)
                    self.state = 154
                    self.expr(0) 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(DashSQLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = DashSQLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(DashSQLParser.RETURN)
            self.state = 161
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_table_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(DashSQLParser.CREATE, 0)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def WITH(self):
            return self.getToken(DashSQLParser.WITH, 0)

        def LPAREN(self):
            return self.getToken(DashSQLParser.LPAREN, 0)

        def column_def_list(self):
            return self.getTypedRuleContext(DashSQLParser.Column_def_listContext,0)


        def RPAREN(self):
            return self.getToken(DashSQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_create_table_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_table_stmt" ):
                listener.enterCreate_table_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_table_stmt" ):
                listener.exitCreate_table_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_table_stmt" ):
                return visitor.visitCreate_table_stmt(self)
            else:
                return visitor.visitChildren(self)




    def create_table_stmt(self):

        localctx = DashSQLParser.Create_table_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_create_table_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(DashSQLParser.CREATE)
            self.state = 164
            self.match(DashSQLParser.ID)
            self.state = 165
            self.match(DashSQLParser.WITH)
            self.state = 166
            self.match(DashSQLParser.LPAREN)
            self.state = 167
            self.column_def_list()
            self.state = 168
            self.match(DashSQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_def_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.Column_defContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.Column_defContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COMMA)
            else:
                return self.getToken(DashSQLParser.COMMA, i)

        def getRuleIndex(self):
            return DashSQLParser.RULE_column_def_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_def_list" ):
                listener.enterColumn_def_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_def_list" ):
                listener.exitColumn_def_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_def_list" ):
                return visitor.visitColumn_def_list(self)
            else:
                return visitor.visitChildren(self)




    def column_def_list(self):

        localctx = DashSQLParser.Column_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_column_def_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.column_def()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 171
                self.match(DashSQLParser.COMMA)
                self.state = 172
                self.column_def()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DashSQLParser.RULE_column_def

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReactiveColumnDefContext(Column_defContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.Column_defContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COLON)
            else:
                return self.getToken(DashSQLParser.COLON, i)
        def type_name(self):
            return self.getTypedRuleContext(DashSQLParser.Type_nameContext,0)

        def EQUALS(self):
            return self.getToken(DashSQLParser.EQUALS, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReactiveColumnDef" ):
                listener.enterReactiveColumnDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReactiveColumnDef" ):
                listener.exitReactiveColumnDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReactiveColumnDef" ):
                return visitor.visitReactiveColumnDef(self)
            else:
                return visitor.visitChildren(self)


    class SimpleColumnDefContext(Column_defContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.Column_defContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)
        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)
        def type_name(self):
            return self.getTypedRuleContext(DashSQLParser.Type_nameContext,0)

        def EQUALS(self):
            return self.getToken(DashSQLParser.EQUALS, 0)
        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleColumnDef" ):
                listener.enterSimpleColumnDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleColumnDef" ):
                listener.exitSimpleColumnDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleColumnDef" ):
                return visitor.visitSimpleColumnDef(self)
            else:
                return visitor.visitChildren(self)



    def column_def(self):

        localctx = DashSQLParser.Column_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_column_def)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = DashSQLParser.SimpleColumnDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(DashSQLParser.ID)
                self.state = 179
                self.match(DashSQLParser.COLON)
                self.state = 180
                self.type_name()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 181
                    self.match(DashSQLParser.EQUALS)
                    self.state = 182
                    self.expr(0)


                pass

            elif la_ == 2:
                localctx = DashSQLParser.ReactiveColumnDefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(DashSQLParser.ID)
                self.state = 186
                self.match(DashSQLParser.COLON)
                self.state = 187
                self.type_name()
                self.state = 188
                self.match(DashSQLParser.EQUALS)
                self.state = 189
                self.match(DashSQLParser.COLON)
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 190
                    self.statement()
                    self.state = 193 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2305843010871839508) != 0)):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(DashSQLParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(DashSQLParser.STRING_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(DashSQLParser.FLOAT_TYPE, 0)

        def DATE_TYPE(self):
            return self.getToken(DashSQLParser.DATE_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(DashSQLParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_name" ):
                listener.enterType_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_name" ):
                listener.exitType_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = DashSQLParser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66571993088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(DashSQLParser.INSERT, 0)

        def TO(self):
            return self.getToken(DashSQLParser.TO, 0)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def where_from_condition(self):
            return self.getTypedRuleContext(DashSQLParser.Where_from_conditionContext,0)


        def insert_row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.Insert_rowContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.Insert_rowContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_insert_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_stmt" ):
                listener.enterInsert_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_stmt" ):
                listener.exitInsert_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_stmt" ):
                return visitor.visitInsert_stmt(self)
            else:
                return visitor.visitChildren(self)




    def insert_stmt(self):

        localctx = DashSQLParser.Insert_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_insert_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(DashSQLParser.INSERT)
            self.state = 200
            self.match(DashSQLParser.TO)
            self.state = 201
            self.match(DashSQLParser.ID)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 202
                self.where_from_condition()


            self.state = 205
            self.match(DashSQLParser.COLON)
            self.state = 207 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 206
                    self.insert_row()

                else:
                    raise NoViableAltException(self)
                self.state = 209 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_from_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(DashSQLParser.WHERE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def FROM(self):
            return self.getToken(DashSQLParser.FROM, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_where_from_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_from_condition" ):
                listener.enterWhere_from_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_from_condition" ):
                listener.exitWhere_from_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_from_condition" ):
                return visitor.visitWhere_from_condition(self)
            else:
                return visitor.visitChildren(self)




    def where_from_condition(self):

        localctx = DashSQLParser.Where_from_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_where_from_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(DashSQLParser.WHERE)
            self.state = 212
            self.match(DashSQLParser.ID)
            self.state = 213
            self.match(DashSQLParser.FROM)
            self.state = 214
            self.match(DashSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(DashSQLParser.Id_listContext,0)


        def EQUALS(self):
            return self.getToken(DashSQLParser.EQUALS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(DashSQLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_insert_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_row" ):
                listener.enterInsert_row(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_row" ):
                listener.exitInsert_row(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_row" ):
                return visitor.visitInsert_row(self)
            else:
                return visitor.visitChildren(self)




    def insert_row(self):

        localctx = DashSQLParser.Insert_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_insert_row)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.id_list()
            self.state = 217
            self.match(DashSQLParser.EQUALS)
            self.state = 218
            self.expr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(DashSQLParser.UPDATE, 0)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def SET(self):
            return self.getToken(DashSQLParser.SET, 0)

        def update_assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.Update_assignmentContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.Update_assignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COMMA)
            else:
                return self.getToken(DashSQLParser.COMMA, i)

        def WHERE(self):
            return self.getToken(DashSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(DashSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_update_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate_stmt" ):
                listener.enterUpdate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate_stmt" ):
                listener.exitUpdate_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_stmt" ):
                return visitor.visitUpdate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def update_stmt(self):

        localctx = DashSQLParser.Update_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_update_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(DashSQLParser.UPDATE)
            self.state = 221
            self.match(DashSQLParser.ID)
            self.state = 222
            self.match(DashSQLParser.SET)
            self.state = 223
            self.update_assignment()
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 224
                    self.match(DashSQLParser.COMMA)
                    self.state = 225
                    self.update_assignment() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 231
                self.match(DashSQLParser.WHERE)
                self.state = 232
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def EQUALS(self):
            return self.getToken(DashSQLParser.EQUALS, 0)

        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_update_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate_assignment" ):
                listener.enterUpdate_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate_assignment" ):
                listener.exitUpdate_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_assignment" ):
                return visitor.visitUpdate_assignment(self)
            else:
                return visitor.visitChildren(self)




    def update_assignment(self):

        localctx = DashSQLParser.Update_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_update_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(DashSQLParser.ID)
            self.state = 236
            self.match(DashSQLParser.EQUALS)
            self.state = 237
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(DashSQLParser.WRITE, 0)

        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def LPAREN(self):
            return self.getToken(DashSQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DashSQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_write_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_stmt" ):
                listener.enterWrite_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_stmt" ):
                listener.exitWrite_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_stmt" ):
                return visitor.visitWrite_stmt(self)
            else:
                return visitor.visitChildren(self)




    def write_stmt(self):

        localctx = DashSQLParser.Write_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_write_stmt)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(DashSQLParser.WRITE)
                self.state = 240
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(DashSQLParser.WRITE)
                self.state = 242
                self.match(DashSQLParser.LPAREN)
                self.state = 243
                self.expr(0)
                self.state = 244
                self.match(DashSQLParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(DashSQLParser.SELECT, 0)

        def column_list(self):
            return self.getTypedRuleContext(DashSQLParser.Column_listContext,0)


        def FROM(self):
            return self.getToken(DashSQLParser.FROM, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def where_condition(self):
            return self.getTypedRuleContext(DashSQLParser.Where_conditionContext,0)


        def AS(self):
            return self.getToken(DashSQLParser.AS, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_stmt" ):
                return visitor.visitSelect_stmt(self)
            else:
                return visitor.visitChildren(self)




    def select_stmt(self):

        localctx = DashSQLParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_select_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(DashSQLParser.SELECT)
            self.state = 249
            self.column_list()
            self.state = 250
            self.match(DashSQLParser.FROM)
            self.state = 251
            self.match(DashSQLParser.ID)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 252
                self.where_condition()


            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 255
                self.match(DashSQLParser.AS)
                self.state = 256
                self.match(DashSQLParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(DashSQLParser.MULT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COMMA)
            else:
                return self.getToken(DashSQLParser.COMMA, i)

        def getRuleIndex(self):
            return DashSQLParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_list" ):
                return visitor.visitColumn_list(self)
            else:
                return visitor.visitChildren(self)




    def column_list(self):

        localctx = DashSQLParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(DashSQLParser.MULT)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(DashSQLParser.ID)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==53:
                    self.state = 261
                    self.match(DashSQLParser.COMMA)
                    self.state = 262
                    self.match(DashSQLParser.ID)
                    self.state = 267
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(DashSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(DashSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_where_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_condition" ):
                listener.enterWhere_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_condition" ):
                listener.exitWhere_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_condition" ):
                return visitor.visitWhere_condition(self)
            else:
                return visitor.visitChildren(self)




    def where_condition(self):

        localctx = DashSQLParser.Where_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_where_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(DashSQLParser.WHERE)
            self.state = 271
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(DashSQLParser.JOIN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def WITH(self):
            return self.getToken(DashSQLParser.WITH, 0)

        def BY(self):
            return self.getToken(DashSQLParser.BY, 0)

        def AND(self):
            return self.getToken(DashSQLParser.AND, 0)

        def AS(self):
            return self.getToken(DashSQLParser.AS, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_join_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_stmt" ):
                listener.enterJoin_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_stmt" ):
                listener.exitJoin_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoin_stmt" ):
                return visitor.visitJoin_stmt(self)
            else:
                return visitor.visitChildren(self)




    def join_stmt(self):

        localctx = DashSQLParser.Join_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_join_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(DashSQLParser.JOIN)
            self.state = 274
            self.match(DashSQLParser.ID)
            self.state = 275
            self.match(DashSQLParser.WITH)
            self.state = 276
            self.match(DashSQLParser.ID)
            self.state = 277
            self.match(DashSQLParser.BY)
            self.state = 278
            self.match(DashSQLParser.ID)
            self.state = 279
            self.match(DashSQLParser.AND)
            self.state = 280
            self.match(DashSQLParser.ID)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 281
                self.match(DashSQLParser.AS)
                self.state = 282
                self.match(DashSQLParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Filter_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(DashSQLParser.FILTER, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def BY(self):
            return self.getToken(DashSQLParser.BY, 0)

        def condition(self):
            return self.getTypedRuleContext(DashSQLParser.ConditionContext,0)


        def AS(self):
            return self.getToken(DashSQLParser.AS, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_filter_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter_stmt" ):
                listener.enterFilter_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter_stmt" ):
                listener.exitFilter_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilter_stmt" ):
                return visitor.visitFilter_stmt(self)
            else:
                return visitor.visitChildren(self)




    def filter_stmt(self):

        localctx = DashSQLParser.Filter_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_filter_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(DashSQLParser.FILTER)
            self.state = 286
            self.match(DashSQLParser.ID)
            self.state = 287
            self.match(DashSQLParser.BY)
            self.state = 288
            self.condition()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 289
                self.match(DashSQLParser.AS)
                self.state = 290
                self.match(DashSQLParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sort_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SORT(self):
            return self.getToken(DashSQLParser.SORT, 0)

        def LT(self):
            return self.getToken(DashSQLParser.LT, 0)

        def DESC(self):
            return self.getToken(DashSQLParser.DESC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def BY(self):
            return self.getToken(DashSQLParser.BY, 0)

        def GT(self):
            return self.getToken(DashSQLParser.GT, 0)

        def AS(self):
            return self.getToken(DashSQLParser.AS, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_sort_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSort_stmt" ):
                listener.enterSort_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSort_stmt" ):
                listener.exitSort_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSort_stmt" ):
                return visitor.visitSort_stmt(self)
            else:
                return visitor.visitChildren(self)




    def sort_stmt(self):

        localctx = DashSQLParser.Sort_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_sort_stmt)
        self._la = 0 # Token type
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(DashSQLParser.SORT)
                self.state = 294
                self.match(DashSQLParser.LT)
                self.state = 295
                self.match(DashSQLParser.DESC)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 296
                    self.match(DashSQLParser.GT)


                self.state = 299
                self.match(DashSQLParser.ID)
                self.state = 300
                self.match(DashSQLParser.BY)
                self.state = 301
                self.match(DashSQLParser.ID)
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 302
                    self.match(DashSQLParser.AS)
                    self.state = 303
                    self.match(DashSQLParser.ID)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(DashSQLParser.SORT)
                self.state = 307
                self.match(DashSQLParser.ID)
                self.state = 308
                self.match(DashSQLParser.BY)
                self.state = 309
                self.match(DashSQLParser.ID)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 310
                    self.match(DashSQLParser.AS)
                    self.state = 311
                    self.match(DashSQLParser.ID)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(DashSQLParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.ID)
            else:
                return self.getToken(DashSQLParser.ID, i)

        def IN(self):
            return self.getToken(DashSQLParser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)


        def DOT2(self):
            return self.getToken(DashSQLParser.DOT2, 0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = DashSQLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_for_stmt)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(DashSQLParser.FOR)
                self.state = 317
                self.match(DashSQLParser.ID)
                self.state = 318
                self.match(DashSQLParser.IN)
                self.state = 319
                self.expr(0)
                self.state = 320
                self.match(DashSQLParser.DOT2)
                self.state = 321
                self.expr(0)
                self.state = 322
                self.match(DashSQLParser.COLON)
                self.state = 324 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 323
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 326 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(DashSQLParser.FOR)
                self.state = 329
                self.match(DashSQLParser.ID)
                self.state = 330
                self.match(DashSQLParser.IN)
                self.state = 331
                self.match(DashSQLParser.ID)
                self.state = 332
                self.match(DashSQLParser.COLON)
                self.state = 334 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 333
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 336 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(DashSQLParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(DashSQLParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = DashSQLParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(DashSQLParser.WHILE)
            self.state = 341
            self.condition()
            self.state = 342
            self.match(DashSQLParser.COLON)
            self.state = 344 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 343
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 346 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(DashSQLParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(DashSQLParser.ConditionContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.COLON)
            else:
                return self.getToken(DashSQLParser.COLON, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(DashSQLParser.ELSE, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = DashSQLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(DashSQLParser.IF)
            self.state = 349
            self.condition()
            self.state = 350
            self.match(DashSQLParser.COLON)
            self.state = 352 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 351
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 354 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 356
                self.match(DashSQLParser.ELSE)
                self.state = 357
                self.match(DashSQLParser.COLON)
                self.state = 359 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 358
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 361 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(DashSQLParser.SWITCH, 0)

        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def case_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.Case_stmtContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.Case_stmtContext,i)


        def default_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.Default_stmtContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.Default_stmtContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_switch_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_stmt" ):
                listener.enterSwitch_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_stmt" ):
                listener.exitSwitch_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_stmt" ):
                return visitor.visitSwitch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def switch_stmt(self):

        localctx = DashSQLParser.Switch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(DashSQLParser.SWITCH)
            self.state = 366
            self.expr(0)
            self.state = 367
            self.match(DashSQLParser.COLON)
            self.state = 370 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 370
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [26]:
                        self.state = 368
                        self.case_stmt()
                        pass
                    elif token in [28]:
                        self.state = 369
                        self.default_stmt()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 372 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DashSQLParser.RULE_case_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CaseExprStmtContext(Case_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.Case_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(DashSQLParser.CASE, 0)
        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseExprStmt" ):
                listener.enterCaseExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseExprStmt" ):
                listener.exitCaseExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseExprStmt" ):
                return visitor.visitCaseExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class CaseIsStmtContext(Case_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.Case_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(DashSQLParser.CASE, 0)
        def IS(self):
            return self.getToken(DashSQLParser.IS, 0)
        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseIsStmt" ):
                listener.enterCaseIsStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseIsStmt" ):
                listener.exitCaseIsStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseIsStmt" ):
                return visitor.visitCaseIsStmt(self)
            else:
                return visitor.visitChildren(self)



    def case_stmt(self):

        localctx = DashSQLParser.Case_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_case_stmt)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = DashSQLParser.CaseIsStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(DashSQLParser.CASE)
                self.state = 375
                self.match(DashSQLParser.IS)
                self.state = 376
                self.expr(0)
                self.state = 377
                self.match(DashSQLParser.COLON)
                self.state = 379 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 378
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 381 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                pass

            elif la_ == 2:
                localctx = DashSQLParser.CaseExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(DashSQLParser.CASE)
                self.state = 384
                self.expr(0)
                self.state = 385
                self.match(DashSQLParser.COLON)
                self.state = 387 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 386
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 389 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(DashSQLParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(DashSQLParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.StatementContext,i)


        def getRuleIndex(self):
            return DashSQLParser.RULE_default_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_stmt" ):
                listener.enterDefault_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_stmt" ):
                listener.exitDefault_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_stmt" ):
                return visitor.visitDefault_stmt(self)
            else:
                return visitor.visitChildren(self)




    def default_stmt(self):

        localctx = DashSQLParser.Default_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_default_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(DashSQLParser.DEFAULT)
            self.state = 394
            self.match(DashSQLParser.COLON)
            self.state = 396 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 395
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 398 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(DashSQLParser.Function_callContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_function_call_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_stmt" ):
                listener.enterFunction_call_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_stmt" ):
                listener.exitFunction_call_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_stmt" ):
                return visitor.visitFunction_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def function_call_stmt(self):

        localctx = DashSQLParser.Function_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_function_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DashSQLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(DashSQLParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)
        def LBRACKET(self):
            return self.getToken(DashSQLParser.LBRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)

        def RBRACKET(self):
            return self.getToken(DashSQLParser.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccessExpr" ):
                listener.enterArrayAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccessExpr" ):
                listener.exitArrayAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessExpr" ):
                return visitor.visitArrayAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(DashSQLParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(DashSQLParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call(self):
            return self.getTypedRuleContext(DashSQLParser.Function_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(DashSQLParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)

        def GT(self):
            return self.getToken(DashSQLParser.GT, 0)
        def LT(self):
            return self.getToken(DashSQLParser.LT, 0)
        def GTE(self):
            return self.getToken(DashSQLParser.GTE, 0)
        def LTE(self):
            return self.getToken(DashSQLParser.LTE, 0)
        def EQ(self):
            return self.getToken(DashSQLParser.EQ, 0)
        def NEQ(self):
            return self.getToken(DashSQLParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class IsExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)

        def IS(self):
            return self.getToken(DashSQLParser.IS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsExpr" ):
                listener.enterIsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsExpr" ):
                listener.exitIsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsExpr" ):
                return visitor.visitIsExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DashSQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)

        def MULT(self):
            return self.getToken(DashSQLParser.MULT, 0)
        def DIV(self):
            return self.getToken(DashSQLParser.DIV, 0)
        def MOD(self):
            return self.getToken(DashSQLParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DashSQLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = DashSQLParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 403
                self.match(DashSQLParser.NOT)
                self.state = 404
                self.expr(4)
                pass

            elif la_ == 2:
                localctx = DashSQLParser.ArrayAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 405
                self.match(DashSQLParser.ID)
                self.state = 406
                self.match(DashSQLParser.LBRACKET)
                self.state = 407
                self.expr(0)
                self.state = 408
                self.match(DashSQLParser.RBRACKET)
                pass

            elif la_ == 3:
                localctx = DashSQLParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 410
                self.function_call()
                pass

            elif la_ == 4:
                localctx = DashSQLParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 411
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 428
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 426
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = DashSQLParser.IsExprContext(self, DashSQLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 414
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 415
                        self.match(DashSQLParser.IS)
                        self.state = 416
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = DashSQLParser.ComparisonExprContext(self, DashSQLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 417
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 418
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 138538465099776) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 419
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = DashSQLParser.AddSubExprContext(self, DashSQLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 420
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 421
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 422
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = DashSQLParser.MulDivExprContext(self, DashSQLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 423
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 424
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 283124244152320) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 425
                        self.expr(6)
                        pass

             
                self.state = 430
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(DashSQLParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(DashSQLParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(DashSQLParser.RPAREN, 0)

        def literal_value(self):
            return self.getTypedRuleContext(DashSQLParser.Literal_valueContext,0)


        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = DashSQLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_atom)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(DashSQLParser.LPAREN)
                self.state = 432
                self.expr(0)
                self.state = 433
                self.match(DashSQLParser.RPAREN)
                pass
            elif token in [56, 57, 58, 59, 60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.literal_value()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.match(DashSQLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DashSQLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DashSQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DashSQLParser.RPAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(DashSQLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return DashSQLParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = DashSQLParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(DashSQLParser.ID)
            self.state = 440
            self.match(DashSQLParser.LPAREN)
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4540332111831236608) != 0):
                self.state = 441
                self.expr_list()


            self.state = 444
            self.match(DashSQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(DashSQLParser.INTEGER, 0)

        def FLOAT_NUM(self):
            return self.getToken(DashSQLParser.FLOAT_NUM, 0)

        def STRING_LIT(self):
            return self.getToken(DashSQLParser.STRING_LIT, 0)

        def TRUE_LIT(self):
            return self.getToken(DashSQLParser.TRUE_LIT, 0)

        def FALSE_LIT(self):
            return self.getToken(DashSQLParser.FALSE_LIT, 0)

        def getRuleIndex(self):
            return DashSQLParser.RULE_literal_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_value" ):
                listener.enterLiteral_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_value" ):
                listener.exitLiteral_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_value" ):
                return visitor.visitLiteral_value(self)
            else:
                return visitor.visitChildren(self)




    def literal_value(self):

        localctx = DashSQLParser.Literal_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literal_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2233785415175766016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DashSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(DashSQLParser.ExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.AND)
            else:
                return self.getToken(DashSQLParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(DashSQLParser.OR)
            else:
                return self.getToken(DashSQLParser.OR, i)

        def getRuleIndex(self):
            return DashSQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DashSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.expr(0)
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 449
                    self.match(DashSQLParser.AND)
                    self.state = 450
                    self.expr(0)
                    self.state = 455
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.expr(0)
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 457
                    self.match(DashSQLParser.OR)
                    self.state = 458
                    self.expr(0)
                    self.state = 463
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




