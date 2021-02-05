graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 9
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 15
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 134
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 59
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 172
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 171
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 167
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 197
  ]
]
