University Scholarship Allocation System Using Python
1. Problem Statement
The University Scholarship Allocation System is designed to evaluate student applications and allocate scholarships to eligible students based on predefined criteria.

The system considers the following factors:
1. Aggregate Marks: Students must score at least 75% in their examinations.
2. Subject-wise Minimum Marks: Students must score at least 60 marks in every subject.
3. Attendance: Students must have at least 75% attendance.
4. Family Income: The annual family income must not exceed ₹2,50,000.
5. Ranking: Eligible students are ranked according to their aggregate percentage in descending order.
6. Tie-Breaking Rules: If two or more students have the same aggregate percentage, the student with higher attendance is ranked first. If attendance is also equal, the student with lower family income is ranked first. If all these criteria are equal, names are arranged alphabetically.
The system displays the list of eligible students in rank order and identifies students who qualify for the scholarship.

Note: The eligibility thresholds and tie-breaking rules used here are illustrative and can be modified according to university policies.
2. Algorithm
Step 1: Start the program.

Step 2: Read the number of student applicants.

Step 3: For each student, input:
- Student name
- Marks obtained in each subject
- Attendance percentage
- Annual family income
Step 4: Calculate the aggregate percentage using the total marks obtained and maximum possible marks.

Step 5: Check the eligibility criteria:
- Aggregate percentage ≥ 75%
- Minimum mark in every subject ≥ 60
- Attendance ≥ 75%
- Annual family income ≤ ₹2,50,000
Step 6: If all the conditions are satisfied, add the student to the eligible applicants list. Otherwise, mark the student as ineligible.

Step 7: Sort the eligible students using the following priority:
1. Higher aggregate percentage first.
2. Higher attendance first.
3. Lower annual family income first.
4. Student name in alphabetical order.
Step 8: Display the ranked list of eligible students with their marks, attendance, income, and rank.

Step 9: If no students are eligible, display an appropriate message.

Step 10: Stop the program.
3. Flowchart
The following flowchart illustrates the complete process of scholarship allocation.
```Mermaid
flowchart TD

    A([Start]) --> B[/Input number of applicants/]
    B --> C[/Input student name, subject marks,<br/>attendance and family income/]
    C --> D[Calculate aggregate percentage]

    D --> E{Aggregate >= 75%<br/>and every subject >= 60?}

    E -- No --> F[Mark student ineligible]
    E -- Yes --> G{Attendance >= 75%<br/>and income <= Rs. 250000?}

    G -- No --> F
    G -- Yes --> H[Add student to eligible list]

    F --> I{More applicants?}
    H --> I

    I -- Yes --> C
    I -- No --> J[Sort eligible students]

    J --> K[Rank by aggregate descending]
    K --> L[Break ties by attendance descending]
    L --> M[Break remaining ties by income ascending]
    M --> N[Break remaining ties alphabetically]

    N --> O{Any eligible students?}

    O -- Yes --> P[/Display ranked eligible students/]
    O -- No --> Q[/Display no eligible students/]

    P --> R([Stop])
    Q --> R

    classDef startEnd fill:#d5f5e3,stroke:#229954,color:#000
    classDef process fill:#d6eaf8,stroke:#2874a6,color:#000
    classDef decision fill:#fcf3cf,stroke:#b7950b,color:#000

    class A,R startEnd
    class B,C,D,F,H,J,K,L,M,N,P,Q process
    class E,G,I,O decision
```
4. Python Source Code
The following Python program accepts student details, checks eligibility, ranks eligible students, and displays the scholarship allocation results.
# University Scholarship Allocation System

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_FAMILY_INCOME = 250000

SUBJECTS = ["Mathematics", "Physics", "Chemistry"]


def evaluate_student(name, marks, attendance, income):
    # Calculate aggregate percentage
    aggregate = sum(marks) / (len(marks) * 100) * 100

    # Check eligibility criteria
    eligible = (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARK for mark in marks)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_FAMILY_INCOME
    )

    return {
        "name": name,
        "marks": marks,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "eligible": eligible
    }


def main():
    students = []

    n = int(input("Enter number of applicants: "))

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Student name: ")

        marks = []
        for subject in SUBJECTS:
            mark = float(input(f"Marks in {subject} (out of 100): "))
            marks.append(mark)

        attendance = float(input("Attendance percentage: "))
        income = float(input("Annual family income (Rs.): "))

        student = evaluate_student(
            name, marks, attendance, income
        )
        students.append(student)

    # Filter eligible students
    eligible_students = [
        student for student in students
        if student["eligible"]
    ]

    # Rank by aggregate descending, attendance descending,
    # income ascending, and name alphabetically.
    eligible_students.sort(
        key=lambda student: (
            -student["aggregate"],
            -student["attendance"],
            student["income"],
            student["name"].casefold()
        )
    )

    print("\n========== SCHOLARSHIP RESULTS ==========")

    if not eligible_students:
        print("No students are eligible for the scholarship.")
    else:
        print("Eligible Students (Ranked):\n")

        for rank, student in enumerate(
            eligible_students, start=1
        ):
            print(f"Rank: {rank}")
            print(f"Name: {student['name']}")
            print(
                f"Aggregate: {student['aggregate']:.2f}%"
            )
            print(
                f"Attendance: {student['attendance']:.2f}%"
            )
            print(
                f"Annual Family Income: Rs. "
                f"{student['income']:.2f}"
            )
            print("-" * 35)

    # Display ineligible students
    ineligible_students = [
        student for student in students
        if not student["eligible"]
    ]

    print("\nIneligible Students:")

    if not ineligible_students:
        print("None")
    else:
        for student in ineligible_students:
            print(
                f"{student['name']} - "
                f"Aggregate: {student['aggregate']:.2f}%"
            )


if __name__ == "__main__":
    main()



Explanation of the Code
- evaluate_student() calculates the aggregate percentage and checks whether the student satisfies all eligibility conditions.
- all() ensures that every subject mark meets the minimum requirement.
- List comprehension separates eligible and ineligible applicants.
- sort() ranks eligible students according to aggregate marks, attendance, income, and alphabetical order.
- enumerate() assigns a rank to each eligible student, starting from 1.
- main() handles input, processing, ranking, and output.
Important: This example assumes three subjects, each carrying 100 marks. The aggregate percentage is calculated as the average of the three subject marks.
5. Sample Input
Consider the following four students applying for the university scholarship.
Enter number of applicants: 4

Enter details for Student 1
Student name: Rahul
Marks in Mathematics (out of 100): 90
Marks in Physics (out of 100): 80
Marks in Chemistry (out of 100): 85
Attendance percentage: 90
Annual family income (Rs.): 180000

Enter details for Student 2
Student name: Anjali
Marks in Mathematics (out of 100): 80
Marks in Physics (out of 100): 85
Marks in Chemistry (out of 100): 90
Attendance percentage: 95
Annual family income (Rs.): 200000

Enter details for Student 3
Student name: Kiran
Marks in Mathematics (out of 100): 70
Marks in Physics (out of 100): 80
Marks in Chemistry (out of 100): 75
Attendance percentage: 80
Annual family income (Rs.): 240000

Enter details for Student 4
Student name: Priya
Marks in Mathematics (out of 100): 90
Marks in Physics (out of 100): 55
Marks in Chemistry (out of 100): 90
Attendance percentage: 95
Annual family income (Rs.): 150000

6. Sample Output
========== SCHOLARSHIP RESULTS ==========

Eligible Students (Ranked):

Rank: 1
Name: Anjali
Aggregate: 85.00%
Attendance: 95.00%
Annual Family Income: Rs. 200000.00
-----------------------------------

Rank: 2
Name: Rahul
Aggregate: 85.00%
Attendance: 90.00%
Annual Family Income: Rs. 180000.00
-----------------------------------

Rank: 3
Name: Kiran
Aggregate: 75.00%
Attendance: 80.00%
Annual Family Income: Rs. 240000.00
-----------------------------------

Ineligible Students:
Priya - Aggregate: 78.33%

Explanation of the Output
- Anjali ranks first because her aggregate is 85% and her attendance is higher than Rahul's.
- Rahul ranks second because he has the same aggregate as Anjali but lower attendance.
- Kiran ranks third because his aggregate is 75%, and he satisfies all the eligibility conditions.
- Priya is ineligible because her Physics marks are 55, which is below the required minimum of 60 marks.
Therefore, three out of the four applicants qualify for the scholarship.
7. Mermaid Flowchart Code
You can copy the following code into the official Mermaid Live Editor to generate a visual flowchart.

Website: Mermaid Live Editor
#chatgpt-mermaid-_r_gr_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_gr_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_gr_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_gr_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-_r_gr_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_gr_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_gr_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_gr_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_gr_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_gr_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_gr_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_gr_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_gr_ p{margin:0;}#chatgpt-mermaid-_r_gr_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_gr_ .label text,#chatgpt-mermaid-_r_gr_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ .node rect,#chatgpt-mermaid-_r_gr_ .node circle,#chatgpt-mermaid-_r_gr_ .node ellipse,#chatgpt-mermaid-_r_gr_ .node polygon,#chatgpt-mermaid-_r_gr_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .rough-node .label text,#chatgpt-mermaid-_r_gr_ .node .label text,#chatgpt-mermaid-_r_gr_ .image-shape .label,#chatgpt-mermaid-_r_gr_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_gr_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .rough-node .label,#chatgpt-mermaid-_r_gr_ .node .label,#chatgpt-mermaid-_r_gr_ .image-shape .label,#chatgpt-mermaid-_r_gr_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_gr_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_gr_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_gr_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-_r_gr_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-_r_gr_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_gr_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-_r_gr_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_gr_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-_r_gr_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_gr_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_gr_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_gr_ .icon-shape,#chatgpt-mermaid-_r_gr_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_gr_ .icon-shape p,#chatgpt-mermaid-_r_gr_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-_r_gr_ .icon-shape .label rect,#chatgpt-mermaid-_r_gr_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_gr_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_gr_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_gr_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_gr_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_gr_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_gr_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_gr_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_gr_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_gr_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_gr_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_gr_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_gr_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_gr_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_gr_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_gr_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_gr_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_gr_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_gr_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_gr_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_gr_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_gr_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_gr_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_gr_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_gr_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .node rect,#chatgpt-mermaid-_r_gr_ .node circle,#chatgpt-mermaid-_r_gr_ .node ellipse,#chatgpt-mermaid-_r_gr_ .node polygon,#chatgpt-mermaid-_r_gr_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_gr_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_gr_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_gr_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_gr_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_gr_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}#chatgpt-mermaid-_r_gr_ .startEnd rect{fill:rgb(213, 245, 227)!important;stroke:rgb(34, 153, 84)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .startEnd polygon{fill:rgb(213, 245, 227)!important;stroke:rgb(34, 153, 84)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .startEnd ellipse{fill:rgb(213, 245, 227)!important;stroke:rgb(34, 153, 84)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .startEnd circle{fill:rgb(213, 245, 227)!important;stroke:rgb(34, 153, 84)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .startEnd path{fill:rgb(213, 245, 227)!important;stroke:rgb(34, 153, 84)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .startEnd tspan{fill:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .process rect{fill:rgb(214, 234, 248)!important;stroke:rgb(40, 116, 166)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .process polygon{fill:rgb(214, 234, 248)!important;stroke:rgb(40, 116, 166)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .process ellipse{fill:rgb(214, 234, 248)!important;stroke:rgb(40, 116, 166)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .process circle{fill:rgb(214, 234, 248)!important;stroke:rgb(40, 116, 166)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .process path{fill:rgb(214, 234, 248)!important;stroke:rgb(40, 116, 166)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .process tspan{fill:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .decision rect{fill:rgb(252, 243, 207)!important;stroke:rgb(183, 149, 11)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .decision polygon{fill:rgb(252, 243, 207)!important;stroke:rgb(183, 149, 11)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .decision ellipse{fill:rgb(252, 243, 207)!important;stroke:rgb(183, 149, 11)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .decision circle{fill:rgb(252, 243, 207)!important;stroke:rgb(183, 149, 11)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .decision path{fill:rgb(252, 243, 207)!important;stroke:rgb(183, 149, 11)!important;color:rgb(0, 0, 0)!important;}#chatgpt-mermaid-_r_gr_ .decision tspan{fill:rgb(0, 0, 0)!important;}StartInput number of applicantsInput student name, subjectmarks,attendance and family incomeCalculate aggregatepercentageAggregate >= 75%and every subject >= 60?Mark student ineligibleAttendance >= 75%and income <= Rs. 250000?Add student to eligible listMore applicants?Sort eligible studentsRank by aggregate descendingBreak ties by attendancedescendingBreak remaining ties by incomeascendingBreak remaining tiesalphabeticallyAny eligible students?Display ranked eligiblestudentsDisplay no eligible studentsStopNoYesNoYesYesNoYesNo




How to Generate the Flowchart
1. Open the Mermaid Live Editor.
2. Select the existing sample code in the editor.
3. Paste the Mermaid code provided above.
4. The flowchart will appear automatically.
5. Export the flowchart as a PNG, SVG, or PDF if required for your assignment.
8. Conclusion
The University Scholarship Allocation System automates the process of evaluating scholarship applications using academic performance, subject-wise minimum marks, attendance, and family income. It identifies eligible students, ranks them according to predefined criteria, and resolves ties consistently
