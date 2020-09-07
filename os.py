"""Non-Preemptive FCFS scheduling """

# ========== calculating completion time ============
def completion_time(ct, bt,n):
    sum = 0
    for i in range(n):
      sum += bt[i]
      ct[i] += sum
      
        
   
#  =========calculating turnAround time ============
def turnAroundTime(ct, tat, at,n):
   
    for i in range(n):
        tat[i] = ct[i] - at[i]
        
   

#  ========== calculating waiting time ============
def waitingTime(tat, wt, bt, n):
    
    for i in range(n):
        wt[i] = tat[i] - bt[i]

        
# ============calculating average waiting time =============
def avgWaiting(wt, n):
   avg = sum(wt) / n
   print("Average waitng time is =  " ,avg," ms") 

n = int(input("Enter the number of processess\n"))


bt = []
at = []
ct = [0]*n
tat = [0]*n
wt = [0]*n

# ====== Taking arrival timmings =========
print("Enter arrival timmings for the processess")
for i in range(n):
    at.append(int(input()))

# T===== Taking burst timmings ==========    
print("Enter burst timmings for the processess in order of process ids")
for i in range(n):
    bt.append(int(input()))
    
# ====calling all the fuctions =========
completion_time(ct, bt,n)
turnAroundTime(ct, tat, at,n)
waitingTime(tat, wt, bt, n)


# ===== Display processes along with all details  =========== 
print("Processes   Burst Time   Arrival Time     Completion",  
      "Time   Turn-Around Time  Waiting Time \n") 

for i in range(n): 
  
     
    print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],  
          "\t\t", ct[i], "\t\t ", tat[i], "\t\t ", wt[i])

# Displaying average waiting time 
print("\n=================================================")
avgWaiting(wt, n)
print("===================================================")
