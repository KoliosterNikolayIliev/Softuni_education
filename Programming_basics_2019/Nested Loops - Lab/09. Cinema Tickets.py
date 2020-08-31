movie=input()
standard_ticket_count=0
kids_ticket_count=0
student_ticket_count=0
total_seats_taken=0
while movie !='Finish':
    free_seats=int(input())
    taken_seats=0
    for seats in range(free_seats):
        ticket_type=input()
        if ticket_type=='End':
            break
        taken_seats+=1
        if ticket_type=='student':
            student_ticket_count+=1
        elif ticket_type=='kid':
            kids_ticket_count+=1
        elif ticket_type=='standard':
            standard_ticket_count+=1

    total_seats_taken+=taken_seats
    percent_taken=taken_seats/free_seats*100
    print(f'{movie} - {percent_taken:.2f}% full.')

    movie = input()

print(f'Total tickets: {total_seats_taken}')
students_percent=student_ticket_count/total_seats_taken*100
print(f'{students_percent:.2f}% student tickets.')

standard_percent=standard_ticket_count/total_seats_taken*100
print(f'{standard_percent:.2f}% standard tickets.')

kids_percent=kids_ticket_count/total_seats_taken*100
print(f'{kids_percent:.2f}% kids tickets.')
