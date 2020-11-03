#By Shanmukh chowdary
#importing required modules
from flask import Flask, request
app = Flask(__name__)
#to display first webpage for selection of tool
@app.route('/')
def index():
    return '''<html style="background-image: url('https://media1.tenor.com/images/8ab51cca650124bdbd211ce2e8fb0714/tenor.gif?itemid=10625836'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1"><title>BI TOOLS BY SHANMUKH</title><style>
.content {
  max-width: 500px;
  margin: auto;
}
</style>
<div class="content">
  <!-- Page content -->

<form action="/index2" method="post" style="background-color:yellow;">
<input type="radio" id="protein" name="type" value="protein" required>
<label for="protein">protein Motif Finding</label><br>
<input type="radio" id="NW" name="type" value="NW">
<label for="NW">Needleman Wunsch Algorithm</label><br>
<input type="radio" id="SW" name="type" value="SW">
<label for="SW">Smith Waterman Algorithm</label><br>
<input type="radio" id="PSSM" name="type" value="PSSM">
<label for="PSSM">Posistion Specific Scoring Matrix</label>
<br>
<input type="radio" id="ORF" name="type" value="translate">
<label for="TT">Translate tool</label><br>
<input type="submit" name= "form" value="GO">
</br>
</form>
</div>
<script SameSite="None; Secure" src="https://static.landbot.io/landbot-widget/landbot-widget-1.0.0.js"></script>
<script>
  var myLandbot = new LandbotPopup({
    index: 'https://chats.landbot.io/v2/H-713928-UTIPQLJ1KCDM4WHM/index.html',
  });
</script><script>
  // Show a proactive message after 1 seconds
  setTimeout(function() {
    myLandbot.sendProactive({
  "message": "Hii",
  "author": "Shanmukh",
  "avatar": "https://storage.googleapis.com/media.helloumi.com/133117/channels/QAKBU8F4ZGUUT6QB1E1QRPQJABINPUF7.jpg",
  "extra": {
    "hide_textbox": true
  }
});
  }, 1000);
</script>
</html>'''
import re
#webpage for collecting input from user
@app.route('/index2',methods=['POST','GET'])
def index2():
    if request.form['type']=='protein':
        return '''<html style="background-image: url('https://media2.giphy.com/media/CRDXaPhEDK5xK/giphy-downsized.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Protein motif finding</title>
<form action="/motif" method="post" enctype="multipart/form-data">
				<h3>Enter the motif pattern</h3>
				<input type="text" name="pattern" required/>
				<h3>Choose fastsa file<h3>
				<input type="file" accept=".fasta" name="file" required>
				<h3>Click here to submit</h3>
                <input type="submit" name= "form" value="Submit" />
</form>
<script SameSite="None; Secure" src="https://static.landbot.io/landbot-widget/landbot-widget-1.0.0.js"></script>
<script>
  var myLandbot = new LandbotPopup({
    index: 'https://chats.landbot.io/v2/H-717160-1VCO6MLCRULB9ZUG/index.html',
  });
</script><script>
  // Show a proactive message after 1 seconds
  setTimeout(function() {
    myLandbot.sendProactive({
  "message": "Need Help!",
  "author": "Motif Bot",
  "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/LxCxE_bound_to_Retinoblastoma.png/350px-LxCxE_bound_to_Retinoblastoma.png",
  "extra": {
    "hide_textbox": true
  }
});
  }, 1000);
</script>
</html>'''
    elif request.form['type']=='NW':
        return '''<html style="background-image: url('https://media2.giphy.com/media/CRDXaPhEDK5xK/giphy-downsized.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">
<h1>Needleman Wunsch Algorithm</h1>
<form action="/nwresult" method="post">
<h3>Enter Sequence 1<input type="text" name="seq1" style="width:500" required></h3>
<h3>Enter Sequence 2<input type="text" name="seq2" style="width:500" required></h3>
<h3>Match score<input type="number" name="match" required>Mismatch score<input type="number" name="mismatch" required>Gap score<input type="number" name="gap" required></h3>
<input type="submit" name= "form" value="Submit">
<script SameSite="None; Secure" src="https://static.landbot.io/landbot-widget/landbot-widget-1.0.0.js"></script>
<script>
  var myLandbot = new LandbotPopup({
    index: 'https://chats.landbot.io/v2/H-717175-62AIY6MRC569EZ6Z/index.html',
  });
</script><script>
  // Show a proactive message after 1 seconds
  setTimeout(function() {
    myLandbot.sendProactive({
  "message": "Need Help!",
  "author": "NW bot",
  "avatar": "https://storage.googleapis.com/media.helloumi.com/brands/helloumi.png",
  "extra": {
    "hide_textbox": true
  }
});
  }, 1000);
</script>
</html>'''
    elif request.form['type']=='SW':
        return '''<html style="background-image: url('https://media2.giphy.com/media/CRDXaPhEDK5xK/giphy-downsized.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">
<h1>Smith Waterman Algorithm</h1>
<form action="/swresult" method="post">
<h3>Enter Sequence 1<input type="text" name="seq1" style="width:500" required></h3>
<h3>Enter Sequence 2<input type="text" name="seq2" style="width:500" required></h3>
<h3>Match score<input type="number" name="match" required>Mismatch score<input type="number" name="mismatch" required>Gap score<input type="number" name="gap" required></h3>
<input type="submit" name= "form" value="Submit">
<script SameSite="None; Secure" src="https://static.landbot.io/landbot-widget/landbot-widget-1.0.0.js"></script>
<script>
  var myLandbot = new LandbotPopup({
    index: 'https://chats.landbot.io/v2/H-717179-G8L2H0U2D9W7NDYF/index.html',
  });
</script><script>
  // Show a proactive message after 1 seconds
  setTimeout(function() {
    myLandbot.sendProactive({
  "message": "Need Help!",
  "author": "SW Bot",
  "avatar": "https://storage.googleapis.com/media.helloumi.com/brands/helloumi.png",
  "extra": {
    "hide_textbox": true
  }
});
  }, 1000);
</script>
</html>'''
    elif request.form['type']=="PSSM":
        return '''<html style="background-image: url('https://media2.giphy.com/media/CRDXaPhEDK5xK/giphy-downsized.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PSSM</title>
<h2>Enter the sequences in fasta format</h2>
Enter all sequences having same length
<p>Example:
<br>
>seq1
<br>
AGACAGATGATAG
<br>
>seq2
<br>
AGACCCTGATGAT
<br>
>seq3
<br>
AGACCCCGATGAT
</p>
<form action="/pssm" method="post">
<textarea name = "seqs" style="width:500;height:300" required></textarea><br>
<h3>Query Sequence</h3>
<input type="text" name="que" required/>
		 <input type="submit" name= "form" value="Submit" />
		 <script SameSite="None; Secure" src="https://static.landbot.io/landbot-widget/landbot-widget-1.0.0.js"></script>
<script>
  var myLandbot = new LandbotPopup({
    index: 'https://chats.landbot.io/v2/H-717188-ON41ZK7UIVH9O97F/index.html',
  });
</script><script>
  // Show a proactive message after 1 seconds
  setTimeout(function() {
    myLandbot.sendProactive({
  "message": "Need Help!",
  "author": "PSSM Bot",
  "avatar": "https://storage.googleapis.com/media.helloumi.com/brands/helloumi.png",
  "extra": {
    "hide_textbox": true
  }
});
  }, 1000);
</script>
</html>'''
    elif request.form['type']=="translate":
        return '''
<html style="background-image: url('https://media2.giphy.com/media/CRDXaPhEDK5xK/giphy-downsized.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">
        <form action="/translate" method="post" enctype="multipart/form-data">
				<h3>Choose fastsa file containing single DNA sequence<h3>
				<input type="file" accept=".fasta" name="file" required>
				<h3>Click here to submit</h3>
                <input type="submit" name= "form" value="Submit" />
                <script SameSite="None; Secure" src="https://static.landbot.io/landbot-widget/landbot-widget-1.0.0.js"></script>
<script>
  var myLandbot = new LandbotPopup({
    index: 'https://chats.landbot.io/v2/H-717195-RPU277YEAJGLDL3S/index.html',
  });
</script><script>
  // Show a proactive message after 1 seconds
  setTimeout(function() {
    myLandbot.sendProactive({
  "message": "Need Help!",
  "author": "Translate bot",
  "avatar": "https://storage.googleapis.com/media.helloumi.com/brands/helloumi.png",
  "extra": {
    "hide_textbox": true
  }
});
  }, 1000);
</script>'''
#To perform PSSM matrix and sending output
@app.route('/pssm',methods=['POST'])
def pssm():
    s1=request.form['seqs'].split('\n')
    que=request.form['que']
    ew='''<html style="background-image: url('https://static.wixstatic.com/media/a1210f_d43d8c83f14c432db3f30b6ccb914c52~mv2.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1"><h3 style="text-align:center">Entered Sequences</h3><p style="text-align:center">'''
    s=[]
    for i in range(len(s1)-1):
        if i%2!=0:
            s.append(list(s1[i].upper()[:len(s1[i])-1]))
    s.append(list(s1[len(s1)-1]))
    for i in s:
        ew=ew+''.join(i)+'<br>'
    ew=ew+'</br></p>'
    A=[]
    T=[]
    G=[]
    C=[]
    import numpy as np
    p=np.array(s).transpose()
    p=p.tolist()
    for i in p:
        A.append(round(i.count('A')/len(s),2))
    for i in p:
        T.append(round(i.count('T')/len(s),2))
    for i in p:
        G.append(round(i.count('G')/len(s),2))
    for i in p:
        C.append(round(i.count('C')/len(s),2))
    aw='<h3 style="text-align:center">Raw Frequency table</h3><table style="border:1px solid black;margin-left:auto;margin-right:auto;" border="1"><tr><th>A</th>'
    a=round(sum(A)/len(A),2)
    t=round(sum(T)/len(T),2)
    g=round(sum(G)/len(G),2)
    c=round(sum(C)/len(C),2)
    for i in A:
        if i!=0:
            aw=aw+'<th>'+str(i)+'</th>'
        else:
            aw=aw+'<th>-</th>'
    aw+='<th>'+str(a)+'</th></tr><tr><th>T</th>'
    for i in T:
        if i!=0:
            aw=aw+'<th>'+str(i)+'</th>'
        else:
            aw=aw+'<th>-</th>'
    aw+='<th>'+str(t)+'</th></tr><tr><th>G</th>'
    for i in G:
        if i!=0:
            aw=aw+'<th>'+str(i)+'</th>'
        else:
            aw=aw+'<th>-</th>'
    aw+='<th>'+str(g)+'</th></tr><tr><th>C</th>'
    for i in C:
        if i!=0:
            aw=aw+'<th>'+str(i)+'</th>'
        else:
            aw=aw+'<th>-</th>'
    aw+='<th>'+str(c)+'</th></tr><tr></table>'
    A=[round(i/a,2)for i in A]
    T=[round(i/t,2)for i in T]
    G=[round(i/g,2)for i in G]
    C=[round(i/c,2)for i in C]
    tw='<h3 style="text-align:center">Normalized table</h3><table style="border:1px solid black;margin-left:auto;margin-right:auto;" border="1"><tr><th>A</th>'
    for i in A:
        if i!=0:
            tw=tw+'<th>'+str(i)+'</th>'
        else:
            tw=tw+'<th>-</th>'
    tw+='<th>'+str(a)+'</th></tr><tr><th>T</th>'
    for i in T:
        if i!=0:
            tw=tw+'<th>'+str(i)+'</th>'
        else:
            tw=tw+'<th>-</th>'
    tw+='<th>'+str(t)+'</th></tr><tr><th>G</th>'
    for i in G:
        if i!=0:
            tw=tw+'<th>'+str(i)+'</th>'
        else:
            tw=tw+'<th>-</th>'
    tw+='<th>'+str(g)+'</th></tr><tr><th>C</th>'
    for i in C:
        if i!=0:
            tw=tw+'<th>'+str(i)+'</th>'
        else:
            tw=tw+'<th>-</th>'
    tw+='<th>'+str(c)+'</th></tr><tr></table>'
    a=[]
    t=[]
    g=[]
    c=[]
    from math import log
    for i in A:
        if i!=0:
            a.append(round(log(i,2),2))
        else:
            a.append(0)
    for i in T:
        if i!=0:
            t.append(round(log(i,2),2))
        else:
            t.append(0)
    for i in G:
        if i!=0:
            g.append(round(log(i,2),2))
        else:
            g.append(0)
    for i in C:
        if i!=0:
            c.append(round(log(i,2),2))
        else:
            c.append(0)
    s=[a,t,g,c]
    gw='<h3 style="text-align:center">Log base 2 values table</h3><table style="border:1px solid black;margin-left:auto;margin-right:auto;" border="1"><tr><th>A</th>'
    for i in a:
            gw=gw+'<th>'+str(i)+'</th>'
    gw+='</tr><tr><th>T</th>'
    for i in t:
            gw=gw+'<th>'+str(i)+'</th>'
    gw+='</tr><tr><th>G</th>'
    for i in g:
            gw=gw+'<th>'+str(i)+'</th>'
    gw+='</tr><tr><th>C</th>'
    for i in c:
            gw=gw+'<th>'+str(i)+'</th>'
    gw+='</tr><tr></table>'
    import numpy as np
    s=np.array(s).transpose()
    s=s.tolist()
    score=0
    for i in range(len(s)):
        if que[i]=='A':
            score+=(s[i][0])
        elif que[i]=='T':
            score+=(s[i][1])
        elif que[i]=='G':
            score+=(s[i][2])
        elif que[i]=='C':
            score+=(s[i][3])
    ru='<h3 style="text-align:center">Sum of log odd scores={}</h3>'.format(score)
    return ew+aw+tw+gw+ru
#To perform Smith Waterman algorithm and sending output
@app.route('/swresult',methods=['POST'])
def swresult():
    import copy
    s1=request.form['seq1']
    s2=request.form['seq2']
    seq1=s1
    seq2=s2
    if len(s1)<len(s2):
        s2,s1=s1,s2
    gapscore=int(request.form['gap'])
    matchscore=int(request.form['match'])
    mismatchscore=int(request.form['mismatch'])
    l1=[0]
    l=[]
    for i in range(1,len(s1)+1):
        l1.append(0)
    for i in range(1,len(s2)+1):
        l.append([l1[i]])
    l=[l1]+l
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j]==s2[i]:
                l[i+1].append(1)
            else:
                l[i+1].append(0)
    o=copy.deepcopy(l)
    for i in range(1,len(l)):
        for j in range(1,len(l[i])):
            if l[i][j]==1:
                b1=(o[i-1][j-1])+matchscore
                b2=(o[i-1][j])+gapscore
                b3=(o[i][j-1])+gapscore
                b4=0
                re=[b1,b2,b3,b4]
                s=""
                if re[0]==max(re):
                    s+="↖"
                if re[1]==max(re):
                    s+="↑"
                if re[2]==max(re):
                    s+="←"
                if re[3]==max(re):
                    s="↖↑←"
                l[i][j]=[s,max(re)]
                o[i][j]=max(re)
            else:
                b1=(o[i-1][j-1])+mismatchscore
                b2=(o[i-1][j])+gapscore
                b3=(o[i][j-1])+gapscore
                b4=0
                re=[b1,b2,b3,b4]
                s=""
                if re[0]==max(re):
                    s+="↖"
                if re[1]==max(re):
                    s+="↑"
                if re[2]==max(re):
                    s+="←"
                if re[3]==max(re):
                    s="↖↑←"
                l[i][j]=[s,max(re)]
                o[i][j]=max(re)
                l[i][j]=[s,max(re)]
                o[i][j]=max(re)
    res='''<html style="background-image: url('https://static.wixstatic.com/media/a1210f_d43d8c83f14c432db3f30b6ccb914c52~mv2.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1"><table style="border:1px solid black;margin-left:auto;margin-right:auto;" border="1"><tr><th> </th><th> </th>'''
    s2=[' ']+list(s2)
    for i in range(len(s1)):
        if i!=len(s1)-1:
            res=res+'<th>'+s1[i]+'</th>'
        else:
            res=res+'<th>'+s1[i]+'</th></tr>'
    for i in range(len(l)):
        res=res+'<tr><th>'+s2[i]+'</th>'
        for j in range(len(l[i])):
            if j!=len(l[i])-1:
                res=res+'<th>'+str(l[i][j])+'</th>'
            else:
                res=res+'<th>'+str(l[i][j])+'</th></tr>'
    return res+'</table><h3>↖↑←=Value derived form Diagonal Cell, Up Cell and Left Cell</h3><h3>↖=Value derived form Diagonal Cell</h3><h3>↑=Value derived form Upper Cell</h3><h3>←=Value derived form LeftCell</h3><h4>Match Score= {0}</h4><h4>Mismatch Score= {1}</h4><h4>Gap Score= {2}</h4><h4>Sequence 1: {3}</h4><h4>Sequence 2: {4}</h4>'.format(matchscore,mismatchscore,gapscore,seq1,seq2)
#To perform Needleman Wunsch algorithm and sending output
@app.route('/nwresult',methods=['POST'])
def nwresult():
    s1=request.form['seq1']
    s2=request.form['seq2']
    seq1=s1
    seq2=s2
    import copy
    s1=list(s1)
    s2=list(s2)
    if len(s1)<len(s2):
        s2,s1=s1,s2
    gapscore=int(request.form['gap'])
    matchscore=int(request.form['match'])
    mismatchscore=int(request.form['mismatch'])
    l1=[0]
    l=[]
    for i in range(1,len(s1)+1):
        l1.append(l1[i-1]+gapscore)
    for i in range(1,len(s2)+1):
        l.append([l1[i]])
    l=[l1]+l
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j]==s2[i]:
                l[i+1].append(1)
            else:
                l[i+1].append(0)
    g=[]
    o=copy.deepcopy(l)
    for i in range(1,len(l)):
        for j in range(1,len(l[i])):
            if l[i][j]==1:
                b1=(o[i-1][j-1])+matchscore
                b2=(o[i-1][j])+gapscore
                b3=(o[i][j-1])+gapscore
                re=[b1,b2,b3]
                s=""
                if re[0]==max(re):
                    s+="↖"
                if re[1]==max(re):
                    s+="↑"
                if re[2]==max(re):
                    s+="←"
                g.append(s)
                l[i][j]=[s,max(re)]
                o[i][j]=max(re)
            else:
                b1=(o[i-1][j-1])+mismatchscore
                b2=(o[i-1][j])+gapscore
                b3=(o[i][j-1])+gapscore
                re=[b1,b2,b3]
                s=""
                if re[0]==max(re):
                    s+="↖"
                if re[1]==max(re):
                    s+="↑"
                if re[2]==max(re):
                    s+="←"
                g.append(s)
                l[i][j]=[s,max(re)]
                o[i][j]=max(re)
    res='''<html style="background-image: url('https://static.wixstatic.com/media/a1210f_d43d8c83f14c432db3f30b6ccb914c52~mv2.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1"><table style="border:1px solid black;margin-left:auto;margin-right:auto;" border="1"><tr><th> </th><th> </th>'''
    s2=[' ']+list(s2)
    for i in range(len(s1)):
        if i!=len(s1)-1:
            res=res+'<th>'+s1[i]+'</th>'
        else:
            res=res+'<th>'+s1[i]+'</th></tr>'
    for i in range(len(l)):
        res=res+'<tr><th>'+s2[i]+'</th>'
        for j in range(len(l[i])):
            if j!=len(l[i])-1:
                res=res+'<th>'+str(l[i][j])+'</th>'
            else:
                res=res+'<th>'+str(l[i][j])+'</th></tr>'
    return res+'</table><h3>↖↑←=Value derived form Diagonal Cell, Up Cell and Left Cell</h3><h3>↖=Value derived form Diagonal Cell</h3><h3>↑=Value derived form Upper Cell</h3><h3>←=Value derived form LeftCell</h3><h4>Match Score= {0}</h4><h4>Mismatch Score= {1}</h4><h4>Gap Score= {2}</h4><h4>Sequence 1: {3}</h4><h4>Sequence 2: {4}</h4>'.format(matchscore,mismatchscore,gapscore,seq1,seq2)
#To perform motif finding and sending output
@app.route('/motif', methods=['POST'])
def motif():
    pattern = request.form['pattern']
    global f
    f = request.files['file']
    f.save(f.filename)
    pattern=pattern.upper()
    s=pattern
    s=s.upper()
    s=s.replace(' ','').replace('-','').replace('X','[A-Z]').replace('{','[^').replace('}',']').replace('(','{').replace(')','}')
    k=list((open(f.filename)))
    g=list((open(f.filename)))[1:]
    g=''.join(g).upper().replace(' ','')
    result=re.finditer(s,g)
    p='''<html style="background-image: url('https://static.wixstatic.com/media/a1210f_d43d8c83f14c432db3f30b6ccb914c52~mv2.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">'''
    su=0
    for i in result:
        p=p+'<tr><th>'+str(i.start()+1)+'</th><th>'+str(i.end())+'</th><th>'+str(i.group())+'</th></tr>'
        su=su+1
    return '<h3 style="text-align:center">No.of motifs found='+str(su)+'</h3><table style="border:1px solid black;margin-left:auto;margin-right:auto;" border="1"><tr><th>start</th><th>end</th><th>matching pattern</th></tr>'+p+'</table><h3>Given sequence</h3><p>{0}</p><p>{1}</p><h3>Given pattern </h3><p>{2}</p></h3>'.format(k[0],g,s)
#To perform translation and sending output
@app.route('/translate',methods=['POST'])
def translate():
    f = request.files['file']
    f.save(f.filename)
    g=list((open(f.filename)))[1:]
    g=''.join(g).upper().replace(' ','')
    def cutter(l):
        a,b,c=[],[],[]
        for i in range(3):
            if i==0:
                for j in range(i,len(l),3):
                    a.append(l[j:j+3])
            if i==1:
                b.append(l[:i])
                for j in range(i,len(l),3):
                    b.append(l[j:j+3])
            if i==2:
                c.append(l[:i])
                for j in range(i,len(l),3):
                    c.append(l[j:j+3])
        return [a,b,c]
    def revcomp(u):
        s=list(u)
        for i in range(len(s)):
            if s[i]=='A':s[i]='U'
            elif s[i]=='U':s[i]='A'
            elif s[i]=='G':s[i]='C'
            elif s[i]=='C':s[i]='G'
        return ''.join(s)[::-1]
    y=g
    y=y.replace(' ','')
    y=y.replace('\n','')
    op=0
    w,c=set(list(y)),['A','G','T','C']
    for i in w:
        if i not in c:
            op=1
    if op==1:
        return 'Enter a valid DNA sequence file'
    else:
        y=y.replace('T','U')
        e=cutter(y)
        f=cutter(revcomp(y))
        codes=[['A','Ala','GCA', 'GCC', 'GCG', 'GCU'],
        ['C','Cys','UGC', 'UGU'],
        ['D','Asp','GAC', 'GAU'],
        ['E','Glu','GAA', 'GAG'],
        ['F','Phe','UUC', 'UUU'],
        ['G','Gly','GGA', 'GGC', 'GGG', 'GGU'],
        ['H','His','CAC', 'CAU'],
        ['I','Ile','AUA', 'AUC', 'AUU'],
        ['K','Lys','AAA', 'AAG'],
        ['L','Leu','CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'],
        ['M','Met','AUG'],
        ['N','Asn','AAC', 'AAU'],
        ['P','Pro','CCA', 'CCC', 'CCG', 'CCU'],
        ['Q','Gln','CAA', 'CAG'],
        ['R','Arg','AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
        ['S','Ser','AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'],
        ['T','Thr','ACA', 'ACC', 'ACG', 'ACU'],
        ['V','Val','GUA', 'GUC', 'GUG', 'GUU'],
        ['W','Trp','UGG'],
        ['Y','Tyr','UAC', 'UAU'],
        ['*','stop','UAA', 'UAG', 'UGA']]
        def code(r):
            q=[]
            for i in r:
                if len(i)==3:
                    for j in codes:
                        if i in j:
                            q.append(j[0])
            return q
        aw='''<html style="background-image: url('https://static.wixstatic.com/media/a1210f_d43d8c83f14c432db3f30b6ccb914c52~mv2.gif'); background-size: cover;"><meta name="viewport" content="width=device-width, initial-scale=1">'''
        for i in range(len(e)):
            aw=aw+('<h3>frame '+str(i+1)+' (5prime to 3prime) </h3><textarea name = "seqs" style="width:1000;height:300" disabled>'+str(code(e[i]))+'</textarea>')
        for i in range(len(f)):
            aw=aw+('<h3>frame '+str(i+1)+' (3prime to 5prime) </h3><textarea name = "seqs" style="width:1000;height:300" disabled>'+str(code(e[i]))+'</textarea>')
        return aw
if __name__ == 'main':
    app.run()
