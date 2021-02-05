graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 11
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 16
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 4
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 176
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 68
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 149
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 143
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 163
  ]
]
