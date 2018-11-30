{\rtf1\ansi\ansicpg1252\cocoartf1561
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Heavy Hitter Algorithm is implemented as follow\
\
1. keep a count on total element N\
\
2. get frequency f of incoming data from count min sketch\
\
3. if f >=  N / k, insert the data into heap and delete the previous occurrence\
\
4, delete all element from heap that has f < N / k\
\
5. scan the heap at the end, return all elements that have f >= N / k}