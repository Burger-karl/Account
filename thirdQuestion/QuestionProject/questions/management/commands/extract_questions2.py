# # from django.core.management.base import BaseCommand
# # import fitz  # PyMuPDF
# # import re

# # class Command(BaseCommand):
# #     help = 'Extract questions and options from the second page of PDF using PyMuPDF and print to the console.'

# #     def handle(self, *args, **kwargs):
# #         pdf_path = r'C:\Users\Kalu Ifeanyi\Python3\Account\PRINCIPLES_OF_ACCOUNTS.pdf'

# #         def extract_questions_from_text(text):
# #             questions_list = []
# #             # Match question and options pattern
# #             question_pattern = r"(\d+)\.\s+(.*?)(?=\s+[A-D]\.)"  # Match question until next option
# #             options_pattern = r"A\.\s*(.*?)\s+B\.\s*(.*?)\s+C\.\s*(.*?)\s+D\.\s*(.*?)(?=\s*\d+\.)"  # Match options until next question

# #             # Extract all questions and options
# #             questions = re.findall(question_pattern, text, re.DOTALL)
# #             options = re.findall(options_pattern, text, re.DOTALL)

# #             for i, (q_num, q_text) in enumerate(questions):
# #                 # Ensure that we have options available for the corresponding question
# #                 if i < len(options):
# #                     a, b, c, d = options[i] if len(options) > i else ("", "", "", "")
# #                     question_data = {
# #                         "question_number": q_num.strip(),
# #                         "question_text": q_text.strip(),
# #                         "option_a": a.strip(),
# #                         "option_b": b.strip(),
# #                         "option_c": c.strip(),
# #                         "option_d": d.strip()
# #                     }
# #                     questions_list.append(question_data)

# #             return questions_list

# #         def extract_questions(pdf_path):
# #             questions_list = []
            
# #             # Open the PDF using PyMuPDF
# #             pdf_document = fitz.open(pdf_path)
            
# #             # Extract only the first page
# #             second_page = pdf_document[1]
# #             width, height = second_page.rect.width, second_page.rect.height

# #             # Define two crop boxes for the left and right columns
# #             left_bbox = fitz.Rect(0, 0, width / 2, height)
# #             right_bbox = fitz.Rect(width / 2, 0, width, height)

# #             # Extract text from both columns on the first page
# #             left_column_text = second_page.get_text("text", clip=left_bbox)
# #             right_column_text = second_page.get_text("text", clip=right_bbox)

# #             # Combine the text from both columns to ensure continuity between questions and options
# #             combined_text = left_column_text + "\n" + right_column_text

# #             # Extract questions from the combined text
# #             questions_list.extend(extract_questions_from_text(combined_text))

# #             # Close the PDF after extraction
# #             pdf_document.close()

# #             return questions_list

# #         # Extract questions from the first page
# #         questions = extract_questions(pdf_path)

# #         # Print extracted questions and options to the console
# #         for question in questions:
# #             print(f"Question {question['question_number']}: {question['question_text']}")
# #             print(f"A: {question['option_a']}")
# #             print(f"B: {question['option_b']}")
# #             print(f"C: {question['option_c']}")
# #             print(f"D: {question['option_d']}")
# #             print("-" * 40)

# #         self.stdout.write(self.style.SUCCESS('Successfully extracted questions from the first page using PyMuPDF.'))





# from django.core.management.base import BaseCommand
# import fitz  # PyMuPDF
# import re

# class Command(BaseCommand):
#     help = 'Extract questions and options from the second page of PDF using PyMuPDF and print to the console.'

#     def handle(self, *args, **kwargs):
#         pdf_path = r'C:\Users\Kalu Ifeanyi\Python3\Account\PRINCIPLES_OF_ACCOUNTS.pdf'

#         def extract_questions_from_text(text):
#             questions_list = []
#             # Match question and options pattern
#             question_pattern = r"(\d+)\.\s+(.*?)(?=\s+[A-D]\.)"  # Match question until next option
#             options_pattern = r"A\.\s*(.*?)\s+B\.\s*(.*?)\s+C\.\s*(.*?)\s+D\.\s*(.*?)(?=\s*\d+\.)"  # Match options until next question

#             # Extract all questions and options
#             questions = re.findall(question_pattern, text, re.DOTALL)
#             options = re.findall(options_pattern, text, re.DOTALL)

#             # Check if question 29 or other questions are missing
#             for question in questions:
#                 if question[0].strip() == '29':
#                     print(f"Question 29 found: {question[1]}")

#             for i, (q_num, q_text) in enumerate(questions):
#                 # Ensure that we have options available for the corresponding question
#                 if i < len(options):
#                     a, b, c, d = options[i] if len(options) > i else ("", "", "", "")
#                     question_data = {
#                         "question_number": q_num.strip(),
#                         "question_text": q_text.strip(),
#                         "option_a": a.strip(),
#                         "option_b": b.strip(),
#                         "option_c": c.strip(),
#                         "option_d": d.strip()
#                     }
#                     questions_list.append(question_data)

#             return questions_list

#         def extract_questions(pdf_path):
#             questions_list = []
            
#             # Open the PDF using PyMuPDF
#             pdf_document = fitz.open(pdf_path)
            
#             # Extract only the second page
#             second_page = pdf_document[1]
#             width, height = second_page.rect.width, second_page.rect.height

#             # Define two crop boxes for the left and right columns
#             left_bbox = fitz.Rect(0, 0, width / 2, height)
#             right_bbox = fitz.Rect(width / 2, 0, width, height)

#             # Extract text from both columns on the second page
#             left_column_text = second_page.get_text("text", clip=left_bbox)
#             right_column_text = second_page.get_text("text", clip=right_bbox)

#             # Combine the text from both columns to ensure continuity between questions and options
#             combined_text = left_column_text + "\n" + right_column_text

#             # Print the raw text around question 29 to debug missing question
#             print("Extracted Text Around Question 29:")
#             start_index = combined_text.find("29.")
#             print(combined_text[start_index:start_index + 200])  # Print some context around question 29

#             # Extract questions from the combined text
#             questions_list.extend(extract_questions_from_text(combined_text))

#             # Close the PDF after extraction
#             pdf_document.close()

#             return questions_list

#         # Extract questions from the second page
#         questions = extract_questions(pdf_path)

#         # Print extracted questions and options to the console
#         for question in questions:
#             print(f"Question {question['question_number']}: {question['question_text']}")
#             print(f"A: {question['option_a']}")
#             print(f"B: {question['option_b']}")
#             print(f"C: {question['option_c']}")
#             print(f"D: {question['option_d']}")
#             print("-" * 40)

#         self.stdout.write(self.style.SUCCESS('Successfully extracted questions from the second page using PyMuPDF.'))



from django.core.management.base import BaseCommand
import fitz  # PyMuPDF
import re
from questions.models import Question  # Import the Question model (adjust 'myapp' to your app name)

class Command(BaseCommand):
    help = 'Extract questions and options from the second page of PDF, delete old data, and populate the database.'

    def handle(self, *args, **kwargs):
        pdf_path = r'C:\Users\Kalu Ifeanyi\Python3\Account\PRINCIPLES_OF_ACCOUNTS.pdf'

        def extract_questions_from_text(text):
            questions_list = []
            # Match question and options pattern
            question_pattern = r"(\d+)\.\s+(.*?)(?=\s+[A-D]\.)"  # Match question until next option
            options_pattern = r"A\.\s*(.*?)\s+B\.\s*(.*?)\s+C\.\s*(.*?)\s+D\.\s*(.*?)(?=\s*\d+\.)"  # Match options until next question

            # Extract all questions and options
            questions = re.findall(question_pattern, text, re.DOTALL)
            options = re.findall(options_pattern, text, re.DOTALL)

            for i, (q_num, q_text) in enumerate(questions):
                # Ensure that we have options available for the corresponding question
                if i < len(options):
                    a, b, c, d = options[i] if len(options) > i else ("", "", "", "")
                    question_data = {
                        "question_number": q_num.strip(),
                        "question_text": f"{q_num.strip()}. {q_text.strip()}",  # Add number to the question text
                        "option_a": a.strip(),
                        "option_b": b.strip(),
                        "option_c": c.strip(),
                        "option_d": d.strip()
                    }
                    questions_list.append(question_data)

            return questions_list

        def extract_questions(pdf_path):
            questions_list = []
            
            # Open the PDF using PyMuPDF
            pdf_document = fitz.open(pdf_path)
            
            # Extract only the second page
            second_page = pdf_document[1]
            width, height = second_page.rect.width, second_page.rect.height

            # Define two crop boxes for the left and right columns
            left_bbox = fitz.Rect(0, 0, width / 2, height)
            right_bbox = fitz.Rect(width / 2, 0, width, height)

            # Extract text from both columns on the second page
            left_column_text = second_page.get_text("text", clip=left_bbox)
            right_column_text = second_page.get_text("text", clip=right_bbox)

            # Combine the text from both columns to ensure continuity between questions and options
            combined_text = left_column_text + "\n" + right_column_text

            # Extract questions from the combined text
            questions_list.extend(extract_questions_from_text(combined_text))

            # Close the PDF after extraction
            pdf_document.close()

            return questions_list

        
        # Extract questions from the second page
        questions = extract_questions(pdf_path)

        # Populate the database with extracted questions and options
        for question in questions:
            Question.objects.create(
                question_text=question['question_text'],  # Number is already included in question_text
                option_a=question['option_a'],
                option_b=question['option_b'],
                option_c=question['option_c'],
                option_d=question['option_d']
            )

        self.stdout.write(self.style.SUCCESS('Successfully extracted questions and populated the database.'))
