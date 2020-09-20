graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 10
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 11
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 191
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 163
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 151
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 94
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 146
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 161
  ]
]
