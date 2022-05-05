# from re import S
from sqlite3 import connect, Error
from django.db import models



def pr(records):
	if len(records) != 0:
		for p in records:
			print(p[1])
	else:
		print("Ошибка. Не найдены записи.")


def question(records):
		temp_result_question = []
		for rec in records:
			answer = input("Подходит ли высказывание для будущего телефона?: " + rec[1] +" (Да/Нет)")
			if answer.lower() == "да":
				temp_result_question.append(rec[0])
		return temp_result_question


	

def read_table_tags():
	try:
		sql_connect = connect('sds/db.sqlite3')
		cursor = sql_connect.cursor()
		print("Connect to base")

		sql_select_query_tags = """SELECT * from tags"""
		cursor.execute(sql_select_query_tags)
		records_tags = cursor.fetchall()
		
		result_question = question(records_tags)
		if len(result_question) != 0:
			sql_select_query = """SELECT * FROM PHONE 
											 JOIN TAG_PHONE ON PHONE.ID = TAG_PHONE.ID_PHONE 
											 WHERE TAG_PHONE.ID_TAG IN (""" + ', '.join(map(str, result_question)) + """)
											 GROUP BY TAG_PHONE.ID_PHONE
											 HAVING COUNT(DISTINCT TAG_PHONE.ID_TAG) = """ + str(len(result_question))
		else:
			sql_select_query = """SELECT * FROM PHONE"""
		cursor.execute(sql_select_query)
		records_phone = cursor.fetchall()
		
		while len(records_phone) == 0:
			if len(records_phone) != 0:
				pr(records_phone)
			else:
				print(result_question)
				result_question = result_question[:-1]
				# print(record)
				# result_question = result_question.pop(record)
				print(result_question)

				if len(result_question) != 0:
					sql_select_query = """SELECT * FROM PHONE 
												JOIN TAG_PHONE ON PHONE.ID = TAG_PHONE.ID_PHONE 
												WHERE TAG_PHONE.ID_TAG IN (""" + ', '.join(map(str, result_question)) + """)
												GROUP BY TAG_PHONE.ID_PHONE
												HAVING COUNT(DISTINCT TAG_PHONE.ID_TAG) = """ + str(len(result_question))
				else:
					sql_select_query = """SELECT * FROM PHONE"""
				cursor.execute(sql_select_query)
				records_phone = cursor.fetchall()
				pr(records_phone)


		

	except Error as error:
		print("Error by connect to base: ", error)
	finally:
		if sql_connect:
			sql_connect.close()
			print("Connect close")

read_table_tags()