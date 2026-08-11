# Last updated: 8/10/2026, 5:24:04 PM
1class FreqStack:
2
3    def __init__(self):
4        self.freq={}
5        self.group={}
6        self.maxfreq=0
7
8    def push(self, val: int) -> None:
9        #get the frequency if not create it in the freq hashmap
10        self.freq[val]=self.freq.get(val,0)+1
11        f=self.freq[val]
12
13        #now include it in the group hashmap
14        if f not in self.group:
15            self.group[f]=[]
16        self.group[f].append(val)
17
18        #update the maxval in the maxfreq
19        self.maxfreq=max(self.maxfreq,f)
20
21    def pop(self) -> int:
22        #popping the mx freq element in the group
23        val= self.group[self.maxfreq].pop()
24
25        #decrease the freq of val
26        self.freq[val]-=1
27
28        #decrease the maxfrequency if the group is empty
29        if not self.group[self.maxfreq]:
30            self.maxfreq-=1
31    
32        return val
33        
34
35
36# Your FreqStack object will be instantiated and called as such:
37# obj = FreqStack()
38# obj.push(val)
39# param_2 = obj.pop()