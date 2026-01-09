from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Check Button
button = soup.find('button', string=lambda t: t and 'Tulis Arab' in t)
if button:
    print("SUCCESS: 'Tulis Arab' button found.")
    if 'openDrawingModal()' in button.get('onclick', ''):
        print("SUCCESS: Button calls openDrawingModal()")
    else:
        print("FAIL: Button does not call openDrawingModal()")
else:
    print("FAIL: 'Tulis Arab' button not found.")

# Check Modal
modal = soup.find('div', id='drawing-modal')
if modal:
    print("SUCCESS: Drawing modal found.")
    canvas = modal.find('canvas', id='draw-canvas')
    if canvas:
        print("SUCCESS: Canvas found inside modal.")
    else:
        print("FAIL: Canvas not found inside modal.")

    # Check Toolbar
    toolbar = modal.find('div', class_='bg-slate-100')
    if toolbar:
        print("SUCCESS: Toolbar found.")
        if toolbar.find('button', title='Undo') and toolbar.find('button', title='Redo') and toolbar.find('button', title='Hapus Semua'):
            print("SUCCESS: All toolbar buttons found.")
        else:
            print("FAIL: Missing some toolbar buttons.")

        if toolbar.find('input', id='pen-size'):
            print("SUCCESS: Pen size slider found.")
        else:
            print("FAIL: Pen size slider not found.")
    else:
        print("FAIL: Toolbar not found.")

else:
    print("FAIL: Drawing modal not found.")

# Check Script Logic
if "const canvas = document.getElementById('draw-canvas');" in html:
    print("SUCCESS: JS logic for canvas initialization found.")
else:
    print("FAIL: JS logic not found.")
