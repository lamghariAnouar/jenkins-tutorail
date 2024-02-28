import fire

def hello(name="World"):
  return "Hello i just finished the jenkins course %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)