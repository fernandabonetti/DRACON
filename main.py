import gym
import envs

#minikube service --namespace=monitoring prometheus

ip = '192.168.39.87'
port = '32590'
container = 'resource-consumer'

env = gym.make('Allocator-v0')
env.render()

'''
collector = rc.Collector(ip, port)
for i in range(0, 300):
  print('Memória:{} bytes'.format(collector.getMemory(container)))
  print('CPU: {}'.format(collector.getCPU(container)))
  time.sleep(1)
'''
