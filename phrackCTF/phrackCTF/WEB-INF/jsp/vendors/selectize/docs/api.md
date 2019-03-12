## Selectize API

Selectize controls can be controlled programmatically via the methods described in this section.
When initializing the control, the "selectize" property is
added on the original &lt;select&gt; / &lt;input&gt; element—this
property points to the underlying Selectize instance.

```js
// initialize the selectize control
var $select = $('select').selectize(options);

// fetch the instance
var selectize = $select[0].selectize;
```

#### Related Topics

- [Event Documentation](events.md)
- [Developing Plugins](plugins.md)

### Methods

<table width="100%">
	<tr>
		<th valign="top" colspan="3" align="left"><a href="#methods_options" name="methods_options">Options</a></th>
	</tr>
	<tr>
		<th valign="top" width="120px" align="left">Method</th>
		<th valign="top" align="left">Description</th>
	</tr>
	<tr>
		<td valign="top"><code>addOption(data)</code></td>
		<td valign="top">Adds an available option. If it already exists, nothing will happen. Note: this does not refresh the options list dropdown (use refreshOptions() for that).</td>
	</tr>
	<tr>
		<td valign="top"><code>updateOption(value, data)</code></td>
		<td valign="top">Updates an option available for selection. If it is visible in the selected items or options dropdown, it will be re-rendered automatically.</td>
	</tr>
	<tr>
		<td valign="top"><code>removeOption(value)</code></td>
		<td valign="top">Removes the option identified by the given value.</td>
	</tr>
	<tr>
		<td valign="top"><code>clearOptions()</code></td>
		<td valign="top">Removes all options from the control.</td>
	</tr>
	<tr>
		<td valign="top"><code>getOption(value)</code></td>
		<td valign="top">Retrieves the jQuery element for the option identified by the given value.</td>
	</tr>
	<tr>
		<td valign="top"><code>getAdjacentOption(value, direction)</code></td>
		<td valign="top">Retrieves the jQuery element for the previous or next option, relative to the currently highlighted option. The "direction" argument should be 1 for "next" or -1 for "previous".</td>
	</tr>
	<tr>
		<td valign="top"><code>refreshOptions(triggerDropdown)</code></td>
		<td valign="top">Refreshes the list of available options shown in the autocomplete dropdown menu.</td>
	</tr>
	<tr>
		<th valign="top" colspan="3" align="left"><a href="#methods_items" name="methods_items">Items</a></th>
	</tr>
	<tr>
		<th valign="top" width="120px" align="left">Method</th>
		<th valign="top" align="left">Description</th>
	</tr>
	<tr>
		<td valign="top"><code>clear()</code></td>
		<td valign="top">Resets / clears all selected items from the control.</td>
	</tr>
	<tr>
		<td valign="top"><code>getItem(value)</code></td>
		<td valign="top">Returns the jQuery element of the item matching the given value.</td>
	</tr>
	<tr>
		<td valign="top"><code>addItem(value)</code></td>
		<td valign="top">"Selects" an item. Adds it to the list at the current caret position.</td>
	</tr>
	<tr>
		<td valign="top"><code>removeItem(value)</code></td>
		<td valign="top">Removes the selected item matching the provided value.</td>
	</tr>
	<tr>
		<td valign="top"><code>createItem(value)</code></td>
		<td valign="top">Invokes the "create" method provided in the selectize options that should provide the data for the new item, given the user input. Once this completes, it will be added to the item list.</td>
	</tr>
	<tr>
		<td valign="top"><code>refreshItems()</code></td>
		<td valign="top">Re-renders the selected item lists.</td>
	</tr>
	<tr>
		<th valign="top" colspan="3" align="left"><a href="#methods_items" name="methods_optgroups">Optgroups</a></th>
	</tr>
	<tr>
		<th valign="top" width="120px" align="left">Method</th>
		<th valign="top" align="left">Description</th>
	</tr>
	<tr>
		<td valign="top"><code>addOptionGroup(id, data)</code></td>
		<td valign="top">Registers a new optgroup for options to be bucketed into. The "id" argument refers to a value of the property in option identified by the "optgroupField" setting.</td>
	</tr>
	<tr>
		<th valign="top" colspan="3" align="left"><a href="#methods_events" name="methods_events">Events</a></th>
	</tr>
	<tr>
		<th valign="top" width="120px" align="left">Method</th>
		<th valign="top" align="left">Description</th>
	</tr>
	<tr>
		<td valign="top"><code>on(event, handler)</code></td>
		<td valign="top">Adds an event listener.</td>
	</tr>
	<tr>
		<td valign="top"><code>off(event, handler)</code></td>
		<td valign="top">Removes an event listener.</td>
	</tr>
	<tr>
		<td valign="top"><code>off(event)</code></td>
		<td valign="top">Removes all event listeners.</td>
	</tr>
	<tr>
		<td valign="top"><code>trigger(event, ...)</code></td>
		<td valign="top">Triggers event listeners.</td>
	</tr>
	<tr>
		<th valign="top" colspan="3" align="left"><a href="#methods_dropdown" name="methods_dropdown">Dropdown</a></th>
	</tr>
	<tr>
		<th valign="top" width="120px" align="left">Method</th>
		<th valign="top" align="left">Description</th>
	</tr>
	<tr>
		<td valign="top"><code>open()</code></td>
		<td valign="top">Shows the autocomplete dropdown containing the available options.</td>
	</tr>
	<tr>
		<td valign="top"><code>close()</code></td>
		<td valign="top">Closes the autocomplete dropdown menu.</td>
	</tr>
	<tr>
		<td valign="top"><code>positionDropdown()</code></td>
		<td valign="top">Calculates and applies the appropriate position of the dropdown.</td>
	</tr>
	<tr>
		<th valign="top" colspan="3" align="left"><a href="#methods_other" name="methods_other">Other</a></th>
	</tr>
	<tr>
		<th valign="top" width="120px" align="left">Method</th>
		<th valign="top" align="left">Description</th>
	</tr>
	<tr>
		<td valign="top"><code>destroy()</code></td>
		<td valign="top">Destroys the control and unbinds event listeners so that it can be garbage collected.</td>
	</tr>
	<tr>
		<td valign="top"><code>load(fn)</code></td>
		<td valign="top">Loads options by invoking the the provided function. The function should accept one argument (callback) and invoke the callback with the results once they are available.</td>
	</tr>
	<tr>
		<td valign="top"><code>focus()</code></td>
		<td valign="top">Brings the control into focus.</td>
	</tr>
	<tr>
		<td valign="top"><code>blur()</code></td>
		<td valign="top">Forces the control out of focus.</td>
	</tr>
	<tr>
		<td valign="top"><code>lock()</code></td>
		<td valign="top">Disables user input on the control (note: the control can still receive focus).</td>
	</tr>
	<tr>
		<td valign="top"><code>unlock()</code></td>
		<td valign="top">Re-enables user input on the control.</td>
	</tr>
	<tr>
		<td valign="top"><code>disable()</code></td>
		<td valign="top">Disables user input on the control completely. While disabled, it cannot receive focus.</td>
	</tr>
	<tr>
		<td valign="top"><code>enable()</code></td>
		<td valign="top">Enables the control so that it can respond to focus and user input.</td>
	</tr>
	<tr>
		<td valign="top"><code>getValue()</code></td>
		<td valign="top">Returns the value of the control. If multiple items can be selected (e.g. &lt;select multiple&gt;), this returns an array. If only one item can be selected, this returns a string.</td>
	</tr>
	<tr>
		<td valign="top"><code>setValue(value)</code></td>
		<td valign="top">Resets the selected items to the given value.</td>
	</tr>
	<tr>
		<td valign="top"><code>setCaret(index)</code></td>
		<td valign="top">Moves the caret to the specified position ("index" being the index in the list of selected items).</td>
	</tr>
	<tr>
		<td valign="top"><code>isFull()</code></td>
		<td valign="top">Returns whether or not the user can select more items.</td>
	</tr>
</table>

### Related Objects

#### Search

<table width="100%">
	<tr>
		<th valign="top" width="120px" align="left">Option</th>
		<th valign="top" align="left">Description</th>
		<th valign="top" width="60px" align="left">Type</th>
	</tr>
	<tr>
		<td valign="top"><code>options</code></td>
		<td valign="top">Original search options.</td>
		<td valign="top"><code>object</code></td>
	</tr>
	<tr>
		<td valign="top"><code>query</code></td>
		<td valign="top">The raw user input.</td>
		<td valign="top"><code>string</code></td>
	</tr>
	<tr>
		<td valign="top"><code>tokens</code></td>
		<td valign="top">An array containing parsed search tokens. A token is an object containing two properties: "string" and "regex".</td>
		<td valign="top"><code>array</code></td>
	</tr>
	<tr>
		<td valign="top"><code>total</code></td>
		<td valign="top">The total number of results.</td>
		<td valign="top"><code>int</code></td>
	</tr>
	<tr>
		<td valign="top"><code>items</code></td>
		<td valign="top">A list of matched results. Each result is an object containing two properties: "score" and "id".</td>
		<td valign="top"><code>array</code></td>
	</tr>
</table>
