from celery_task import send_email, send_msg

result = send_email.delay("yuan")
print(result.id)

result2 = send_msg.delay("alex")
print(result2.id)
