#!/bin/bash
for i in `seq 1 100`;
do
	mysql -uroot -e "INSERT INTO answer_db.question_post (title, text,  author_id, added_at) VALUES ('title$i', 'query_post_text$i',  '1', NOW());"
done
for i in `seq 1 100`;
do
	mysql -uroot -e "INSERT INTO answer_db.qa_answer (question_id, text,  author_id, added_at) VALUES ('100', 'answer $i',  '1', NOW());"
done
