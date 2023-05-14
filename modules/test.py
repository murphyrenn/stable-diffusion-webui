import gradio as gr

def my_function(input1):
    # Your function logic here
    return f"You entered: {input1}"

# Create input and output components
input_component = gr.inputs.Textbox(lines=2, label="Input Text")
output_component = gr.outputs.Textbox(label="Output Text")

# Create a tab with input and output components
tab1 = gr.Tab(components=[input_component, output_component], title="Tab 1", id="my_tab1")

# Create a button using the HTML component to toggle the visibility of the entire tab
toggle_button = gr.inputs.HTML("""
<button id="toggle_button" onclick="toggle_visibility()">Toggle Tab 1 Visibility</button>
<script>
  function toggle_visibility() {
    let tabs = document.getElementsByClassName("gradio-tabs")[0].childNodes;
    let target_tab;
    for (let i = 0; i < tabs.length; i++) {
      if (tabs[i].textContent === "Tab 1") {
        target_tab = tabs[i];
        break;
      }
    }

    if (target_tab.style.display === "none") {
      target_tab.style.display = "block";
    } else {
      target_tab.style.display = "none";
    }
  }
</script>
""")

# Create a tab with the toggle button
tab2 = gr.Tab(components=[toggle_button], title="Settings")

# Create the interface with the tabs
iface = gr.Interface(fn=my_function, inputs=gr.TabbedInterface([tab1, tab2]), outputs=output_component)
iface.launch()
