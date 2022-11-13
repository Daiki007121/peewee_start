from database import Thread

thread = Thread.select()
print(thread[0].name)
print(thread[3].name)

thread = Thread.select().where(Thread.name == "Keisuke01").get()
print(threads.name, threads.title, threads.body)
