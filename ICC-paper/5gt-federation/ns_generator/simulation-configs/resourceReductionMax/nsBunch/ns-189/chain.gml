graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 8
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 14
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 10
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 1
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 79
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 116
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 96
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 91
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 73
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 126
  ]
]
