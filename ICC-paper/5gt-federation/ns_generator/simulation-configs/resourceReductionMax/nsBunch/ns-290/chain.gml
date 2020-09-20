graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 4
    memory 3
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 13
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 117
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 181
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 167
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 164
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 104
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 152
  ]
]
