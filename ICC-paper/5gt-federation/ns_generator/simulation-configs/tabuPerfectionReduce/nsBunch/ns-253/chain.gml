graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 13
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 2
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 96
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 85
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 108
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 84
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 168
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 87
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 73
  ]
]
