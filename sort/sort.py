from django.db import models
from s_slots.models import Slot
from .models import Gaandu,Gaandu_theory

def sort_me():
	test=Slot.objects.latest('id')
	num_items=test.id
	for i in range(num_items,0,-1):
		l=Slot.objects.get(id=i)
		if l.Tuesday==False:
			if l.Saturday==False:
				if l.Monday==False:
					print(i)
					Gaandu.objects.create(Name=l.Name,
						Monday=l.Monday,
						Monday_time=l.Monday_time,
						Tuesday=l.Tuesday,
						Tuesday_time=l.Tuesday_time,
						Wednesday=l.Wednesday,
						Wednesday_time=l.Wednesday_time,
						Thursday=l.Thursday,
						Thursday_time=l.Thursday_time,
						Friday=l.Friday,
						Friday_time=l.Friday_time,
						Saturday=l.Saturday,
						Saturday_time=l.Saturday_time,
						)
					y=l.Name
					if y[0]!='L':
						Gaandu_theory.objects.create(Name=l.Name,
						Monday=l.Monday,
						Monday_time=l.Monday_time,
						Tuesday=l.Tuesday,
						Tuesday_time=l.Tuesday_time,
						Wednesday=l.Wednesday,
						Wednesday_time=l.Wednesday_time,
						Thursday=l.Thursday,
						Thursday_time=l.Thursday_time,
						Friday=l.Friday,
						Friday_time=l.Friday_time,
						Saturday=l.Saturday,
						Saturday_time=l.Saturday_time,
						)


