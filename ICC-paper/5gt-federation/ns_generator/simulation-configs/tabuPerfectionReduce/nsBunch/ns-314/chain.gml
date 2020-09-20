graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 16
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 9
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 2
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 50
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 183
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 93
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 68
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 163
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 160
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 153
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 116
  ]
]
