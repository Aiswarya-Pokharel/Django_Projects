from django.shortcuts import render,redirect
# Create your views here.
def home(request):
  result = None

  if request.method == "POST":
    temperature = float(request.POST.get('temperature'))
    scale = request.POST.get('scale')
    if scale == 'C':
      # Celsius to Fahrenheit
      converted = (temperature * 9/5) + 32
      result = f"{temperature}°C = {converted:.2f}°F"
        
    elif scale == 'F':
      # Fahrenheit to Celsius
      converted = (temperature - 32) * 5/9
      result = f"{temperature}°F = {converted:.2f}°C"
    # Store result in session and redirect
    request.session['result'] = result
    return redirect('home')  # ← redirects to GET request

    # On GET, fetch result from session then clear it
  result = request.session.pop('result', None)
  return render(request,'converter.html', {'result': result})