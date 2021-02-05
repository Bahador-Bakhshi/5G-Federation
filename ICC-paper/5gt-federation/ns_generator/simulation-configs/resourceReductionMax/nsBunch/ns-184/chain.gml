graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 16
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 15
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 133
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 118
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 82
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 134
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 129
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 95
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 172
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 158
  ]
]
