f = open("convert_dictionary.html","w")

name_email = {'david': 'david@gmail.com', 'hafid': 'hafid@gmail.com', 'nathalie': 'nathalie@gmail.com', 'najib': 'najib@gmail.com'}
String = ""

for x, y  in name_email.items():
    String = String + "<tr>" + "\n" + "<td>" + x + "</td>" + "\n" + "<td>" + y + "</td>" + "\n" + "</tr>" + "\n"

f.write('''
    <html>
        <head>
            <style>
                table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1.5em;
                font-family: sans-serif;
                min-width: 400px;
                box-shadow: 0 0 80px rgba(0, 0, 0, 0.15);
                }
                td 
                {
                text-align: center; 
                vertical-align: middle;
                }
             </style>
            <title>HTML File</title>
        </head> 
        <body>
        <table>
            <tr>
                <th>Name</th>
                <th>Email</th>
            </tr>
            ''' + String + '''    
        </table>
        </body>
    </html>
    ''')

f.close()
