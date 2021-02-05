graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 10
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 10
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 3
    memory 16
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 152
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 148
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 183
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 136
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 74
  ]
]
