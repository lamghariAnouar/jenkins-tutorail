import fire

def hello(name="World"):
  return "Hellooà %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)