graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 14
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 5
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 15
  ]
  node [
    id 5
    label 6
    disk 2
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
    delay 32
    bw 177
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 179
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 119
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 173
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 152
  ]
]
