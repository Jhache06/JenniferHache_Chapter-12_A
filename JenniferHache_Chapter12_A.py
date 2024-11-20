import csv
import numpy as np


def get_data(filename):
    # create an empty list to store the data
    data = []

    # open the CSV file in reading mode r
    with open(filename, mode='r') as file:
        # create a CSV reader object
        csvreader = csv.reader(file)

        # read the first row. skip header
        header = next(csvreader)

        # Loop through each row in the CSV file
        for row in csvreader:
            # get only the grades
            # change the grades to floating point numbers
            # the grades start from index 2 for row in the csvreader:

            grades = [float(x) for x in row[2:]]

            # add the grades list to data list
            data.append(grades)

    # convert the data list to a numpy array and return it
    return np.array(data)

def calc_statistics(exam_data):
    # list of exams - only goes up to 3
    exams = ['Exam 1', 'Exam 2', 'Exam 3']

    # iterate over each exam to get results
    for i, exam in enumerate(exams):
        # get the grades for the exam
        exam_grades = exam_data[:, i]

        # calculate statistics for the exam
        mean = np.mean(exam_grades)
        median = np.median(exam_grades)
        std_dev = np.std(exam_grades)
        min_grade = np.min(exam_grades)
        max_grade = np.max(exam_grades)

        # print each statistic calc with explanation as a formatted string
        print(f"\nStatistics for {exam}:")
        print(f"  Mean: {mean:.2f}")
        print(f"  Median: {median:.2f}")
        print(f"  Standard Deviation: {std_dev:.2f}")
        print(f"  Minimum: {min_grade:.2f}")
        print(f"  Maximum: {max_grade:.2f}")


def all_statistics(exam_data):
    # flatten the entire dataset to convert grades as a single list (1D array)
    all_grades = exam_data.flatten()

    # calculate the overall statistics for all grades combined
    mean_grade = np.mean(all_grades)
    median_grade = np.median(all_grades)
    std_deviation = np.std(all_grades)
    min_grade = np.min(all_grades)
    max_grade = np.max(all_grades)

    # print the overall statistics
    print("\nStatistics across all exams:")
    print(f"Mean: {mean_grade:.2f}")
    print(f"Median: {median_grade:.2f}")
    print(f"Standard Deviation: {std_deviation:.2f}")
    print(f"Minimum: {min_grade:.2f}")
    print(f"Maximum: {max_grade:.2f}")


def pass_fail_counts(exam_data):
    # Define the passing grade threshold
    pass_threshold = 60

    # Calculate the number of students passing each exam
    pass_counts = np.sum(exam_data >= pass_threshold, axis=0)

    # Calculate the number of students failing each exam
    fail_counts = exam_data.shape[0] - pass_counts

    # List of exams
    exams = ['Exam 1', 'Exam 2', 'Exam 3']

    # Loop over each exam and print the pass/fail counts
    for i, exam in enumerate(exams):
        # Print the results for each exam
        print(f"\n{exam} Pass/Fail Count:")
        print(f"Passed: {pass_counts[i]}")
        print(f"Failed: {fail_counts[i]}")


def overall_pass_percentage(exam_data):
    # calculate overall pass percentage (passing grade must be >= 60 for all exams)
    pass_grade = 60
    total_passes = np.sum(exam_data >= pass_grade)
    total_grades = exam_data.size
    pass_percentage = (total_passes / total_grades) * 100

    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")

# create main function
def main():
    filename = 'grades.csv'
    # Load the data into a numpy array
    exam_data = get_data(filename)

    # print the first few rows of the dataset
    print(f"\nFirst few rows of the dataset:")
    print(exam_data[:10])  # Print first 10 rows for inspection

    # print the statistics for each exam
    calc_statistics(exam_data)

    # print overall statistics across all exams
    all_statistics(exam_data)

    # print the number of students passing and failing the exams
    pass_fail_counts(exam_data)

    # print the overall pass percentage across all exams
    overall_pass_percentage(exam_data)


if __name__ == "__main__":
    main()
