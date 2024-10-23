import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from typing import List, Union, Callable, Optional

__all__ = [
    'stylable_slider',
    'stylable_selectbox',
    'stylable_multiselect',
    'stylable_text_input',
    'stylable_text_area',
    'stylable_button',
    'stylable_progress',
    'stylable_tabs',
    'stylable_expander',
    'stylable_image'
]

def validate_css_styles(css_styles: Optional[Union[str, List[str]]]) -> List[str]:
    """Validate and return CSS styles as a list."""
    if css_styles is None:
        return []
    if isinstance(css_styles, str):
        return [css_styles]
    if isinstance(css_styles, list):
        return css_styles
    raise ValueError("css_styles must be a string or a list of strings.")

def stylable_component(component_func: Callable, key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """
    Create a stylable component with a given Streamlit function.

    Args:
        component_func (Callable): The Streamlit component function to wrap.
        key (str): A unique key for the component.
        css_styles (Optional[Union[str, List[str]]]): CSS styles to apply.
        *args: Positional arguments for the component.
        **kwargs: Keyword arguments for the component.

    Returns:
        The result of the component function.
    
    Raises:
        ValueError: If the key is empty or css_styles is invalid.
    """
    if not key:
        raise ValueError("The 'key' must be a non-empty string.")
    
    css_styles = validate_css_styles(css_styles)
    
    with stylable_container(key, css_styles):
        return component_func(*args, **kwargs)

def stylable_slider(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable slider component."""
    return stylable_component(st.slider, key, css_styles, *args, **kwargs)

def stylable_selectbox(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable selectbox component."""
    return stylable_component(st.selectbox, key, css_styles, *args, **kwargs)

def stylable_multiselect(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable multiselect component."""
    return stylable_component(st.multiselect, key, css_styles, *args, **kwargs)

def stylable_text_input(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable text input component."""
    return stylable_component(st.text_input, key, css_styles, *args, **kwargs)

def stylable_text_area(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable text area component."""
    return stylable_component(st.text_area, key, css_styles, *args, **kwargs)

def stylable_button(label: str, key: str, css_styles: Optional[Union[str, List[str]]] = None, *args, **kwargs):
    """Stylable button component."""
    return stylable_component(st.button, key, css_styles, label=label, *args, **kwargs)


def stylable_progress(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable progress component."""
    return stylable_component(st.progress, key, css_styles, *args, **kwargs)

def stylable_tabs(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable tabs component."""
    return stylable_component(st.tabs, key, css_styles, *args, **kwargs)

def stylable_expander(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable expander component."""
    return stylable_component(st.expander, key, css_styles, *args, **kwargs)

def stylable_image(key: str, css_styles: Optional[Union[str, List[str]]], *args, **kwargs):
    """Stylable image component."""
    return stylable_component(st.image, key, css_styles, *args, **kwargs)
