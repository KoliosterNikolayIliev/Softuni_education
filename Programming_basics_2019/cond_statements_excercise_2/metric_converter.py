number = float(input())
input_metrics = input('')
output_metrics = input('')

if input_metrics == 'mm' and output_metrics == 'm':
    number = number * 0.001
elif input_metrics == 'm' and output_metrics == 'cm':
    number = number * 100
elif input_metrics == 'm' and output_metrics == 'mm':
    number = number * 1000
elif input_metrics == 'mm' and output_metrics == 'cm':
    number = number * 0.1
elif input_metrics == 'cm' and output_metrics == 'mm':
    number = number * 10
elif input_metrics == 'cm' and output_metrics == 'm':
    number = number * 0.01
print(f'{number:.3f}')
