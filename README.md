# School_District_Analysis.

Performing an analysis using school and student data to inform a school district on their budget and priorities.

## Challenge
The school district discovered that the standardized test scores for ninth grade students at Thomas High School were incorrect, and they requested for updated data summaries. After further discussion, it was best to only replace the ninth grade math and reading scores at Thomas High School while keeping all other data associated with this student group intact.

Both math and reading scores were replaced with "NaN", which represents a "Not-a-Number" value, for 461 student records. Although this may seem like a significant number, these score replacements did not alter data summaries tremendously overall.


![Screen Shot 2021-11-14 at 7 56 52 PM](https://user-images.githubusercontent.com/59430635/141706584-c2e0925d-0a74-4f67-9287-f83ba804987a.png)
## Top Five Performing Schools
![Screen Shot 2021-11-14 at 8 17 09 PM](https://user-images.githubusercontent.com/59430635/141707661-7d3d809d-f21b-4b26-be55-6b3f5f4b8c7c.png)

## Bottom Five Performing Schools
![Screen Shot 2021-11-14 at 8 16 53 PM](https://user-images.githubusercontent.com/59430635/141707635-b0f5383b-984f-4cc1-83e1-dd8d599eb378.png)


## Average Math Scores by Grade & School
![Screen Shot 2021-11-14 at 8 02 43 PM](https://user-images.githubusercontent.com/59430635/141706840-04502d6c-4a56-4c85-a614-7f45ebdf9cbb.png)
## Average Reading Scores by Grade & School
![Screen Shot 2021-11-14 at 8 11 13 PM](https://user-images.githubusercontent.com/59430635/141707293-96f7f634-8942-4062-802b-539d12fb9577.png)

Both the average math and reading score summaries were stratisfied by school and grade level. As shown above, the summary tables display "NaN" for ninth grade at Thomas High School whereas the remaining data remained intact.

## School Spending Summary
![Screen Shot 2021-11-14 at 8 04 09 PM](https://user-images.githubusercontent.com/59430635/141706914-1993df5f-dffa-4cd3-bba6-73ca88301beb.png)

When reviewing the School Spending summary, this data change did not impact the spending ranges for either the average math scores or average reading scores. However, this data change did impact the spending ranges for passing percentages. According to the summary above, there was a 6% decrease in % passing math, a 7% decrease in % passing reading, and a 6% decrease in % overall passing in the $630-644 spending range.

## School Size Summary
![Screen Shot 2021-11-14 at 8 04 50 PM](https://user-images.githubusercontent.com/59430635/141706941-119eb36e-a2aa-48e4-b8f2-29f0886e776c.png)

When reviewing the School Size summary, removing the ninth grade scores did not affect the average math and reading scores, but it did affect the passing percentages for medium-sized schools (1,000-2,000). In this category, % passing math, % passing reading, and % overall passing dropped 6% each. Before the data change, the School Size summary showed that medium-sized school had a high performance (91% overall passing) compared to small (90% overall passing) and large schools (58% overall passing). Given the data change, medium size school are the second in performance (85% overall passing).

## School Type Summary
![Screen Shot 2021-11-14 at 8 06 00 PM](https://user-images.githubusercontent.com/59430635/141707007-539366f0-755b-4c78-bda4-4cb8f01546a2.png)
In reviewing the last summary on School Types, this data change also affected the passing percentages that compared charter and district schools. Fortunately, it did not affect the average scores for these two school types. Removing the scores resulted in a reduction in charter school's passing percentages. Before the data change, charter schools had very high passing percentages: 94% passing math, 97% passing reading, 90% overall passing. After the data change, charter schools now have a 90% passing math, 93% passing reading, 87% overall passing. On the plus side, these rates are still far superior when compared to district schools.


