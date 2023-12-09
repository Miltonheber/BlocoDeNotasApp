<h1>NoteApp</h1>
<p>Este é um aplicativo Web que tem como objectivo permitir a escrita de notas apartir de qualquer dispositivo móvel que suporte um mavegador.<br>
O NoteApp foi desenvolvido com as seguintes tecnologias:<br><Hong>Frontend: Html5, CSS & Bootstrap5</strong><br><strong>Backend: Python(Django)</strong></p>

<h1>Passos para rodar a webApp</h1>
<p>1. Clonar o repositório. :)</p>
<p>2. Criar um ambiente virtual, pode ser com a biblioteca virtualenv(<small>pip install virtualenv</small>)</p>
<p>3. Instalar as dependências do projecto, para tal pode usar o arquivo requirements.txt(<small>pip install -r requirements.txt</small>)</p>
<p>4. Activar o ambiente virtual.</p>
<p>5. Criar as migrações do aplicativo note, usando o comando: python manage.py makemigrations note</p>
<p>6. Fazer o migrate das migrações criadas, para que de facto sejam criadas tabelas para o aplicativo, comando: python manage.py migrate note</p>
<p>7. Fazer o migrate das outras aplicações que por padrão com o Django, comando: python manage.py migrate</p>
<p>8. Rodar o projecto com o comando: python manage.py runserver</p>