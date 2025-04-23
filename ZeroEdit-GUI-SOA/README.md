### **Zero Edit - A Peer-to-Peer Event-Driven Text Editor**  

**Zero Edit** is a lightweight, decentralized, and **real-time collaborative text editor** designed for **local Wi-Fi-based peer-to-peer (P2P) editing**. Built in **React**, it enables multiple users to edit files together **without requiring internet access** or a centralized server. Instead, it leverages **local peer connections**, ensuring **low latency** and **secure collaboration** in isolated environments.

---

### **Key Features**
1. **Decentralized P2P Editing**  
   - Uses **WebRTC** (or a similar P2P framework) for **direct communication** between peers.
   - **No central server** needed—ideal for offline-first use cases.
  
2. **Event-Driven Synchronization**  
   - Edits are propagated as **real-time events** to connected peers.
   - Conflict-Free Replicated Data Types (**CRDTs**) ensure seamless collaboration.

3. **Minimalist & Developer-Friendly UI**  
   - Monaco Editor (used in **VS Code**) for a **smooth editing experience**.
   - Side panel for **file management** and **user list**.

4. **Session Sharing via Link**  
   - A **sharable link** will be generated in the **main screen**.
   - Other users can join the session by clicking the link over the local network.

5. **Lightweight & Fast**  
   - Optimized for performance with a **React-based frontend**.
   - **No unnecessary dependencies**, making it efficient for local collaboration.

---

### **User Flow**
1. The **host** creates a session and gets a sharable link.  
2. Other users connect via the link, establishing **direct P2P connections**.  
3. **Edits sync in real-time**, and changes are propagated instantly across all peers.  
4. The session runs **without an internet connection**, relying solely on local Wi-Fi.

---

Would you like a **React-based code template** to kickstart the project? 🚀