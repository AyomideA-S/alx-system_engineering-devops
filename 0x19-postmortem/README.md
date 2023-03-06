# Postmortem

## My first postmortem

### **Issue Summary**

Duration: 2 hours, from 10:00 AM to 12:00 PM WAT (West African Time).

Impact: Users of our e-commerce website experienced slow page load times and some users were unable to complete purchases during the outage. Approximately 20% of users were affected.

Root Cause: An increase in traffic caused a bottleneck in our web application servers, leading to slow response times and some requests timing out.

### **Timeline**

* 10:00 AM: Our monitoring system alerted us to a spike in traffic to our website.
* 10:05 AM: An engineer noticed that the website was responding slowly and reported it to the team.
* 10:10 AM: We initially suspected that the issue was related to our load balancers and began investigating that area of the system.
* 10:30 AM: We ruled out the load balancers as the cause and began investigating the web application servers.
* 11:00 AM: We discovered that the web application servers were experiencing a bottleneck due to the increased traffic.
* 11:15 AM: We attempted to scale up the number of web application servers, but the issue persisted.
* 11:30 AM: We escalated the incident to our DevOps team.
* 12:00 PM: The issue was resolved when the DevOps team discovered and fixed a configuration issue with the web application servers.

### **Root Cause and Resolution**

The root cause of the issue was an increase in traffic that overwhelmed our web application servers, causing slow response times and some requests to time out. The issue was fixed by the DevOps team, who discovered and corrected a misconfiguration in the server settings that had caused the bottleneck.

### **Corrective and Preventative Measures**

To prevent similar issues in the future, we will implement the following measures:

* Scale up our web application servers in anticipation of traffic spikes.
* Add more monitoring and alerting to our systems to detect bottlenecks more quickly.
* Conduct regular load testing to identify and address potential performance issues before they affect users.
* Develop and implement a more robust disaster recovery plan to minimize the impact of future outages.

Tasks to Address the Issue:

* Review and optimize server settings to prevent similar configuration issues in the future.
* Implement auto-scaling for web application servers to automatically adjust to traffic spikes.
* Add additional monitoring and alerting for web application server performance.
* Conduct regular load testing to ensure adequate performance under high traffic conditions.
* Develop and implement a comprehensive disaster recovery plan.