graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 11
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 76
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 162
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 172
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 83
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 142
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 85
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 169
  ]
]
