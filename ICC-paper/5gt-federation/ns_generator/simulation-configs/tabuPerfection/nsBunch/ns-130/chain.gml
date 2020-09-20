graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 6
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 6
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 4
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 3
    memory 1
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 3
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 156
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 195
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 79
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 63
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 181
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 131
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 122
  ]
]
