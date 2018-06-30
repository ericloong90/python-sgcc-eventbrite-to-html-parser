# Python Script to Parse EventBrite Links to HTML-Ready Code for  SG Code Campus

- Script requires an EventBrite developer token to run, please contact repository owner or create your own EventBrite developer token if you are using it from your own EventBrite events. 
- Generated HTML code is only for SG Code Campus website, and no support to add options for customized HTML templates yet (to be implemented in the future, MAYBE)
- `main.py` is the entry point for this script, developed using Python 3.6.5. The following code shows how to run this script:

```bash
./main.py -i input.txt -o output.txt
```
- `input.txt` should contain lines of EventBrite links, while `output.txt` is where the parsed HTML code will be. 