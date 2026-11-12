import os,sys,json,urllib.request as H
L=os.getenv('MAKEFUN_ENV_URL') or sys.exit()
def R(p,d=None):
 q=H.Request(L+p,data=json.dumps(d or {}).encode(),headers={'Content-Type':'application/json'})
 try:return json.load(H.urlopen(q))
 except:raise SystemExit
W=(100,320,330,500,900,0);N=25000;B=[0]*128;S=1;C=0;E=-1;Y=[]
def F(f):
 global B,S,C,E
 B=[0]*128;p=0
 for r in reversed(f.split()[0].split('/')):
  for c in r:
   if c.isdigit():p+=int(c)
   else:B[p]=('PNBRQK'.find(c)+1) if c.isupper() else -('pnbrqk'.find(c)+1);p+=1
  p=(p//16+1)*16
 s=f.split();S=1 if s[1]=='w' else -1
 C=('K' in s[2])+2*('Q' in s[2])+4*('k' in s[2])+8*('q' in s[2])
 E=(int(s[3][1])-1)*16+ord(s[3][0])-97 if s[3]!='-' else -1
def G(cap=False):
 o=[]
 def A(f,t):
  r=0 if S<0 else 7
  if t//16==r:
   for q in (5,4,3,2):o.append((f,t,q*S))
  else:o.append((f,t,0))
 for f in range(128):
  if f&8:continue
  x=B[f]
  if not x or x*S<=0:continue
  a=abs(x)
  if a==1:
   d=16*S;t=f+d
   if 0<=t<128 and not t&8 and not B[t] and not cap:
    A(f,t)
    if (f//16==1 and S>0 or f//16==6 and S<0) and not B[f+2*d]:o.append((f,f+2*d,0))
   for df in (-1,1):
    u=t+df
    if 0<=u<128 and not u&8 and (B[u]*S<0 or u==E):A(f,u)
  elif a<3 or a==6:
   for d in (-31,-33,-14,-18,14,18,31,33) if a==2 else (-17,-16,-15,-1,1,15,16,17):
    t=f+d
    if 0<=t<128 and not t&8 and (B[t]*S<0 if cap else B[t]*S<=0):o.append((f,t,0))
  else:
   for d in (-17,-15,15,17) if a==3 else (-16,-1,1,16) if a==4 else (-17,-16,-15,-1,1,15,16,17):
    t=f+d
    while 0<=t<128 and not t&8:
     if B[t]:
      if B[t]*S<0:o.append((f,t,0))
      break
     if not cap:o.append((f,t,0))
     t+=d
 if not cap:
  if S>0:
   if C&1 and not B[5] and not B[6] and B[7]==4 and not X(4,-1) and not X(5,-1):o.append((4,6,0))
   if C&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not X(4,-1) and not X(3,-1):o.append((4,2,0))
  else:
   if C&4 and not B[117] and not B[118] and B[119]==-4 and not X(116,1) and not X(117,1):o.append((116,118,0))
   if C&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and not X(116,1) and not X(115,1):o.append((116,114,0))
 return o
def X(q,w):
 global S
 o=S;S=w;d=not B[q]
 if d:B[q]=-w
 r=any(t==q for _,t,_ in G(True))
 if d:B[q]=0
 S=o
 return r
D={4:3,0:2,7:1,112:8,116:12,119:4}
def M(f,t,pr):
 global C,E,S
 c=B[t];ep=0
 if B[f]==S and t==E and not c:
  ep=1;c=B[t-16*S];B[t-16*S]=0
 Y.append((f,t,c,pr,C,E,ep))
 B[t]=pr if pr else B[f];B[f]=0
 if abs(B[t])==6 and abs(t-f)==2:
  r=t+1 if t>f else t-2;s=t-1 if t>f else t+1;B[r]=0;B[s]=4*S
 E=(f+t)//2 if abs(B[t])==1 and abs(t-f)==32 else -1
 C&=~(D.get(f,0)|D.get(t,0))
 S=-S
def U():
 global C,E,S
 f,t,c,pr,oc,oe,ep=Y.pop()
 S=-S
 if abs(B[t])==6 and abs(t-f)==2:
  r=t-1 if t>f else t+1;s=t+1 if t>f else t-2;B[r]=0;B[s]=4*S
 B[f]=B[t] if not pr else S
 B[t]=c*(1-ep)
 if ep:B[t-16*S]=-S
 C,E=oc,oe
def K(w):
 return next((f for f in range(128) if B[f]==6*w),-1)
def V():
 s=0
 for f in range(128):
  if f&8:continue
  x=B[f]
  if x:
   a=abs(x);v=W[a-1]
   s+=v if x>0 else -v
 return s*S
T=0
def Z(a,b):
 s=V()
 if s>=b:return b
 if s>a:a=s
 for f,t,pr in G(True):
  M(f,t,pr)
  if X(K(-S),S):
   U();continue
  v=-Z(-b,-a)
  U()
  if v>=b:return b
  if v>a:a=v
 return a
def A(d,a,b):
 global T
 T+=1
 if T>N:raise StopIteration
 if d<=0:return Z(a,b)
 m=G()
 m.sort(key=lambda mv:W[abs(B[mv[1]])-1]*10-W[abs(B[mv[0]])-1],reverse=True)
 for f,t,pr in m:
  M(f,t,pr)
  if X(K(-S),S):
   U();continue
  v=-A(d-1,-b,-a)
  U()
  if v>=b:return b
  if v>a:a=v
 return a
u=lambda s:chr(97+s%16)+str(s//16+1)
def main():
 global T
 while 1:
  g=R('/game',{})
  if g.get('status')=='done':break
  F(g['fen']);bs=None;T=0
  for dp in range(1,30):
   try:
    bb=None;bv=-999999
    for f,t,pr in G():
     M(f,t,pr)
     if X(K(-S),S):
      U();continue
     v=-A(dp-1,-999999,999999)
     U()
     if v>bv:bv=v;bb=(f,t,pr)
    if bb:bs=bb
   except StopIteration:break
  if not bs:bs=G()[0]
  f,t,pr=bs
  R('/move',{'game':g['game'],'move':u(f)+u(t)+('nbrq'[abs(pr)-2] if pr else '')})
if __name__=='__main__':main()
