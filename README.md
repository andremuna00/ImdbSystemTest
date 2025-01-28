# 🎥 IMDb-Like Web Application Performance Analysis 🚀

👋 Welcome to the **IMDb-Like Web Application Performance and Scalability Analysis** project! This system was developed to analyze, test, and optimize the performance of a web application resembling Amazon's IMDb platform.

![image](https://github.com/user-attachments/assets/687d8554-9056-494b-a055-0b026723db9d)

---

## 📝 **Project Overview**

This project dives deep into the **performance evaluation** of a Flask-based 🌐 web application designed to:  
- 🎬 Search for movie titles  
- 📋 Display details like writers, directors, year of publishing, ratings, and actors  
- 💾 Utilize a replica of the IMDb database  

---

## 🧪 **Experimental Setup**

The system involves two machines:

### 1️⃣ **System Under Test (SUT)**  
🏠 Runs the application services.  

🔧 **Frameworks/Libraries**:  
- **Flask** for request management.  
- **Polars** for data processing (efficient handling of CSV files with lazy evaluation and parallel computation).  

⚙️ **Specifications**:  
- 💻 AMD Ryzen 7 3700x @ 3.6GHz  
- 🧠 16GB RAM  
- 📂 NVMe SSD  

### 2️⃣ **Testing Machine**  
📈 Simulates user behavior using **Tsung**.  

⚙️ **Specifications**:  
- 💻 Intel Core i7-8750H @ 2.20GHz  
- 🧠 16GB RAM  
- 📂 NVMe SSD  

---

## 🏗️ **System Architecture**

✨ This system is modeled as an **interactive queuing network**, featuring:  
- Infinite server queue for "thinking" 🧠  
- Two **M/G/1/PS queues** for **Flask** and **Database**  
- A **single-class system** to simplify analysis and maintain statistical uniformity  

⚖️ **Key Assumption**: Processor Sharing (PS) discipline approximates OS scheduling policies, ensuring results' theoretical robustness.

---

## 📊 **Performance Analysis and Metrics**

### ⚡ **Test Setup**
1. 🚶‍♂️ **User Arrival**: Simulated users arrive based on a Poisson process, ensuring no unnatural congestion.  
2. 🔄 **Cyclic Requests**: Users interact with the system:  
   - Visit the homepage 🏠  
   - Search for a movie 🔎  
   - View movie details 🎥  

### 📈 **Results**
- Response times ⏱️ were analyzed using **Tsung**.  
- Database operations proved to be the bottleneck 🚨, consuming the majority of resources.  

---

## 🔧 **System Optimization**

To enhance scalability:  
1. **Database Replication** 📀: Distributed workload across 4 replicas.  
2. **Random Dispatcher** 🎲: Balanced traffic across database replicas.  

📊 Results after optimization:  
- Bottleneck shifted to Flask, improving scalability.  
- Optimal user count increased from 4.1 to 14.5 🚀.  

---

## 🛠️ **Tools and Techniques Used**

- **Frameworks**: Flask, Polars  
- **Load Testing**: Tsung  
- **Theoretical Models**: Queuing theory, MVA 📐  
- **Simulation Tools**: Java Modelling Tools (JMT) 🛠️  

---

## ⚙️ **Getting Started**

### 🛠️ **What You Need**  
To get started with this project, make sure you have the following:  
- 🐍 Python installed.  
- Install Flask: `pip install flask`  
- Install Polars with additional dependencies: `pip install polars[numpy,pandas,pyarrow]`


### ▶️ **Commands to Run the Application**

- 🚀 To start the application: `flask run`  
- 🛠️ To run in debug mode on Windows:  
  1. Set the debug mode: `set FLASK_DEBUG=1`  
  2. Start the app: `flask run`  
- 🌐 To run the server and make it accessible over the network: `flask run --host=0.0.0.0`

---

## 🎯 **Future Improvements**

✨ Explore advanced dispatching disciplines.  
✨ Experiment with database sharding for further scalability.  

---

## 🧑‍🤝‍🧑 **Contributors**

💡 **Giovanni Costa**  
💡 **Andrea Munarin**

---

## 🎉 **Conclusion**

This project highlights the power of **theoretical analysis** and **practical performance testing** for building scalable web applications. With careful design and optimization, we achieved significant performance improvements while maintaining simplicity and robustness.

---

⭐ **Thank you for checking out our project!** 💻 Feel free to reach out for any questions or collaborations. 🌟
