PROMPT_TEMPLATE = """Task: Generate a complete, modern website based on the following requirements. 
Provide the HTML, CSS, and JavaScript in separate markdown code blocks.

### Website Description:
{description}

### Design Requirements:
- Primary Color: {primary_color}
- Secondary Color: {secondary_color}
- Font Family: {font_family}
- Layout Style: {layout_style}
- Include Animations: {include_animation}
- Dark Mode Support: {dark_mode}
- Number of Sections: {num_sections}

### Output Guidelines:
1. Create a responsive, accessible website
2. Use modern CSS (Flexbox/Grid)
3. Include proper semantic HTML
4. Make sure the design is visually appealing
5. If animations are requested, use subtle, performant animations
6. If dark mode is requested, include a toggle switch and appropriate styling

### Required Sections (adjust based on number of sections requested):
1. Hero section with headline and call-to-action
2. Features/Benefits section
3. Testimonials/Reviews section
4. Pricing section (if applicable)
5. Contact/CTA section
6. Footer with basic links

Please generate the complete code with HTML, CSS, and JavaScript in separate code blocks below:

```html
<!-- Your HTML code here -->
```

```css
/* Your CSS code here */
```

```javascript
// Your JavaScript code here */
```"""