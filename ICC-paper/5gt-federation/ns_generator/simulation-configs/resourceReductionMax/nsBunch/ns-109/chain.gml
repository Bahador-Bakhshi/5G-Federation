graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 3
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 181
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 141
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 193
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 129
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 72
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 152
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 115
  ]
]
