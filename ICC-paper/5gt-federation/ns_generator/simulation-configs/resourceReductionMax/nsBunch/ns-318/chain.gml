graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 15
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 2
    memory 2
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 2
    memory 15
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 87
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 191
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 137
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 158
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 52
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 98
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 187
  ]
]
