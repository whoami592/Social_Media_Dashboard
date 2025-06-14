import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from datetime import datetime

class SocialMediaDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Dashboard - Coded by Pakistani Ethical Hacker Mr Sabaz ali Khan")
        self.root.geometry("1200x700")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#1e1e2f")
        self.style.configure("TLabel", background="#1e1e2f", foreground="#ffffff", font=("Arial", 12))
        self.style.configure("Header.TLabel", font=("Arial", 24, "bold"), foreground="#00ff00")
        
        # Create main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Banner
        self.banner_label = ttk.Label(
            self.main_frame,
            text="Social Media Dashboard\nCoded by Pakistani Ethical Hacker Mr Sabaz ali Khan",
            style="Header.TLabel"
        )
        self.banner_label.pack(pady=20)
        
        # Metrics Frame
        self.metrics_frame = ttk.Frame(self.main_frame)
        self.metrics_frame.pack(fill="x", pady=10)
        
        # Sample metrics
        metrics = [
            ("Followers", "125.6K", "+5.2%"),
            ("Engagement", "8.7%", "+1.2%"),
            ("Impressions", "1.2M", "+3.5%"),
            ("Clicks", "15.4K", "+2.8%")
        ]
        
        for i, (title, value, change) in enumerate(metrics):
            metric_frame = ttk.Frame(self.metrics_frame)
            metric_frame.pack(side="left", padx=10, fill="x", expand=True)
            
            ttk.Label(metric_frame, text=title, font=("Arial", 12, "bold")).pack()
            ttk.Label(metric_frame, text=value, font=("Arial", 18, "bold"), foreground="#00ff00").pack()
            ttk.Label(metric_frame, text=change, font=("Arial", 10), foreground="#00ff00").pack()
        
        # Graph Frame
        self.graph_frame = ttk.Frame(self.main_frame)
        self.graph_frame.pack(fill="both", expand=True, pady=20)
        
        # Create sample data for graphs
        self.create_graphs()
        
        # Control Panel
        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill="x", pady=10)
        
        ttk.Button(
            self.control_frame,
            text="Refresh Data",
            command=self.refresh_data
        ).pack(side="left", padx=10)
        
        ttk.Label(
            self.control_frame,
            text=f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ).pack(side="left", padx=10)
    
    def create_graphs(self):
        # Sample data
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        followers = [100, 120, 115, 130, 125, 140, 150]
        engagement = [5, 6, 5.5, 7, 6.5, 8, 8.5]
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        fig.patch.set_facecolor('#1e1e2f')
        
        # Followers graph
        ax1.plot(days, followers, color='#00ff00', marker='o')
        ax1.set_title('Weekly Followers', color='white')
        ax1.set_facecolor('#2d2d44')
        ax1.tick_params(colors='white')
        ax1.grid(True, color='gray', alpha=0.3)
        
        # Engagement graph
        ax2.plot(days, engagement, color='#00ff00', marker='o')
        ax2.set_title('Weekly Engagement', color='white')
        ax2.set_facecolor('#2d2d44')
        ax2.tick_params(colors='white')
        ax2.grid(True, color='gray', alpha=0.3)
        
        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def refresh_data(self):
        # Clear existing graphs
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Recreate graphs with new random data
        self.create_graphs()
        
        # Update timestamp
        for widget in self.control_frame.winfo_children():
            if isinstance(widget, ttk.Label) and "Last Updated" in widget.cget("text"):
                widget.configure(text=f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaDashboard(root)
    root.mainloop()