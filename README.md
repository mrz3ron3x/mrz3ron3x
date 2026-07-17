<div align="center">
  <svg width="240" height="240" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00f0ff" />
        <stop offset="100%" stop-color="#0055ff" />
      </linearGradient>
    </defs>
    <!-- Outer Ring -->
    <circle cx="120" cy="120" r="100" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="4 8" opacity="0.4">
      <animateTransform attributeName="transform" type="rotate" from="0 120 120" to="360 120 120" dur="24s" repeatCount="indefinite"/>
    </circle>
    <!-- Middle Ring -->
    <circle cx="120" cy="120" r="75" fill="none" stroke="#0055ff" stroke-width="1.5" stroke-dasharray="15 10" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="360 120 120" to="0 120 120" dur="18s" repeatCount="indefinite"/>
    </circle>
    <!-- Inner Core -->
    <circle cx="120" cy="120" r="20" fill="url(#cyanGrad)" opacity="0.8">
      <animate attributeName="r" values="18;22;18" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
    </circle>
    <!-- Core Glow -->
    <circle cx="120" cy="120" r="35" fill="none" stroke="#00f0ff" stroke-width="0.5" opacity="0.3">
      <animate attributeName="r" values="30;45;30" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4;0;0.4" dur="3s" repeatCount="indefinite"/>
    </circle>
  </svg>

  <h1 style="font-size: 48px; letter-spacing: 4px; margin-top: -20px; color: #e6edf3;">ZERONEX</h1>
  <p style="font-size: 16px; color: #8b949e; letter-spacing: 1px; margin-top: -10px;">
    Building intelligent systems, developer tools, and digital experiences.
  </p>
</div>

---

### <span style="color: #00f0ff;">//</span> SYSTEM OVERVIEW

I am a developer and AI systems builder based in Pakistan, focused on engineering modern web experiences, developer tools, automation systems, and AI-powered software. My work bridges the gap between complex backend logic and intuitive frontend interfaces, with a strong emphasis on desktop agents and experimental intelligent systems.

I am the founder of **NEX AI**, an evolving personal desktop AI agent designed to connect intelligence with the operating system, tools, workflows, and everyday computing.

---

### <span style="color: #00f0ff;">//</span> NEX AI ARCHITECTURE

NEX AI is not a basic chatbot; it is an evolving AI system engineered to interact directly with the desktop environment, manage complex workflows, and execute tools autonomously.

<div align="center">
  <svg width="100%" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width: 600px;">
    <style>
      .node { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 4; }
      .node-core { fill: #0d1117; stroke: #ff003c; stroke-width: 2; rx: 4; }
      .text { fill: #e6edf3; font-family: monospace; font-size: 12px; text-anchor: middle; dominant-baseline: middle; }
      .text-core { fill: #ff003c; font-family: monospace; font-size: 14px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
      .line { fill: none; stroke: #30363d; stroke-width: 1.5; }
      .line-active { fill: none; stroke: #00f0ff; stroke-width: 1.5; stroke-dasharray: 6 6; }
    </style>
    
    <!-- Connection Lines -->
    <path class="line-active" d="M 300 50 L 300 100">
      <animate attributeName="stroke-dashoffset" from="12" to="0" dur="1s" repeatCount="indefinite"/>
    </path>
    <path class="line-active" d="M 250 130 L 100 130 L 100 180">
      <animate attributeName="stroke-dashoffset" from="12" to="0" dur="1s" repeatCount="indefinite"/>
    </path>
    <path class="line-active" d="M 300 130 L 300 180">
      <animate attributeName="stroke-dashoffset" from="12" to="0" dur="1s" repeatCount="indefinite"/>
    </path>
    <path class="line-active" d="M 350 130 L 500 130 L 500 180">
      <animate attributeName="stroke-dashoffset" from="12" to="0" dur="1s" repeatCount="indefinite"/>
    </path>
    <path class="line" d="M 100 210 L 100 240 L 250 240 L 250 260"/>
    <path class="line" d="M 300 210 L 300 260"/>
    <path class="line" d="M 500 210 L 500 240 L 350 240 L 350 260"/>

    <!-- Nodes -->
    <rect class="node" x="250" y="20" width="100" height="30"/>
    <text class="text" x="300" y="35">USER</text>

    <rect class="node" x="250" y="100" width="100" height="30"/>
    <text class="text" x="300" y="115">INTELLIGENCE</text>

    <rect class="node" x="50" y="180" width="100" height="30"/>
    <text class="text" x="100" y="195">MEMORY</text>

    <rect class="node" x="250" y="180" width="100" height="30"/>
    <text class="text" x="300" y="195">TOOLS</text>

    <rect class="node" x="450" y="180" width="100" height="30"/>
    <text class="text" x="500" y="195">DESKTOP</text>

    <rect class="node-core" x="200" y="260" width="200" height="40"/>
    <text class="text-core" x="300" y="280">NEX AI CORE</text>
  </svg>
</div>

**Core Capabilities:**
*   **Desktop Interaction:** Direct UI automation and system-level control.
*   **AI-Assisted Workflows:** Context-aware task execution and management.
*   **Tool Execution:** Seamless integration with local and external development tools.
*   **Persistent Memory:** Long-term context retention across sessions *(in development)*.
*   **Modular Architecture:** Extensible plugin and agent system *(in development)*.

---

### <span style="color: #00f0ff;">//</span> TECHNOLOGY STACK

<div align="center">
  <h4 style="color: #8b949e; text-transform: uppercase; letter-spacing: 2px; font-size: 12px;">Frontend</h4>
  <a href="#"><img src="https://img.shields.io/badge/HTML5-0d1117?style=flat-square&logo=html5&logoColor=00f0ff" alt="HTML5"></a>
  <a href="#"><img src="https://img.shields.io/badge/CSS3-0d1117?style=flat-square&logo=css3&logoColor=00f0ff" alt="CSS3"></a>
  <a href="#"><img src="https://img.shields.io/badge/JavaScript-0d1117?style=flat-square&logo=javascript&logoColor=00f0ff" alt="JavaScript"></a>
  
  <h4 style="color: #8b949e; text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin-top: 20px;">Backend & Runtime</h4>
  <a href="#"><img src="https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=node.js&logoColor=00f0ff" alt="Node.js"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=00f0ff" alt="Python"></a>
  
  <h4 style="color: #8b949e; text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin-top: 20px;">Systems & Automation</h4>
  <a href="#"><img src="https://img.shields.io/badge/Shell-0d1117?style=flat-square&logo=gnu-bash&logoColor=00f0ff" alt="Shell"></a>
  <a href="#"><img src="https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=00f0ff" alt="Linux"></a>
  <a href="#"><img src="https://img.shields.io/badge/AI%20Agents-0d1117?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzAwZjBmZiI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4em0tMS0xM2gydjZoLTJ6bTAgOGgydjJoLTJ6Ii8+PC9zdmc+&logoColor=00f0ff" alt="AI Agents"></a>
</div>

---

### <span style="color: #00f0ff;">//</span> DEVELOPER PHILOSOPHY

> **"Build systems, not just interfaces."**
> 
> Software should be useful, intelligent, and engineered to solve real problems. I focus on creating robust tools and automated systems that extend human capability, prioritizing clean architecture, reliability, and seamless user experiences over superficial trends.

---

### <span style="color: #00f0ff;">//</span> AFFILIATIONS

**TEAM ATHEX**  
*Member of a technical community focused on advanced systems, collaborative engineering, and experimental software development.*

---

### <span style="color: #00f0ff;">//</span> CURRENTLY BUILDING

- [x] **NEX AI** - Core architecture and desktop integration.
- [x] **Intelligent Automation** - Workflow optimization and tool execution scripts.
- [x] **Developer Tools** - CLI utilities and environment configurations.
- [ ] **AI-Powered Systems** - Expanding persistent memory and modular agent capabilities.
- [ ] **Modern Web Experiences** - High-performance, minimal frontend interfaces.

---

### <span style="color: #00f0ff;">//</span> SYSTEM METRICS

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=zeronex&show_icons=true&theme=transparent&title_color=00f0ff&text_color=8b949e&icon_color=0055ff&bg_color=0d1117&hide_border=true&show=reviews,prs_merged,prs_merged_percentage" alt="GitHub Stats" style="max-width: 100%;">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=zeronex&theme=transparent&hide_border=true&background=0d1117&stroke=30363d&ring=00f0ff&fire=ff003c&currStreakLabel=00f0ff" alt="GitHub Streak" style="max-width: 100%;">
</div>

---

<div align="center">
  <svg width="420" height="130" viewBox="0 0 420 130" xmlns="http://www.w3.org/2000/svg">
    <rect width="420" height="130" fill="#0d1117" stroke="#30363d" stroke-width="1" rx="6"/>
    <text x="15" y="25" fill="#8b949e" font-family="monospace" font-size="13">
      <tspan fill="#00f0ff">&gt; SYSTEM STATUS:</tspan> BUILDING
    </text>
    <text x="15" y="50" fill="#8b949e" font-family="monospace" font-size="13">
      <tspan fill="#00f0ff">&gt; NEX CORE:</tspan> EVOLVING
    </text>
    <text x="15" y="75" fill="#8b949e" font-family="monospace" font-size="13">
      <tspan fill="#00f0ff">&gt; LOCATION:</tspan> PAKISTAN
    </text>
    <text x="15" y="100" fill="#8b949e" font-family="monospace" font-size="13">
      <tspan fill="#00f0ff">&gt; AWAITING INPUT</tspan>
      <tspan fill="#00f0ff">_
        <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
      </tspan>
    </text>
  </svg>
</div>
