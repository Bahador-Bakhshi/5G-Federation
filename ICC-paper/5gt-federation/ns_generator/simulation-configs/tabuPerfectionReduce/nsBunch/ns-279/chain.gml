graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 6
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 10
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 15
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 2
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 129
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 79
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 171
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 112
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 156
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 65
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 82
  ]
]
